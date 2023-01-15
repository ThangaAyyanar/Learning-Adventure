(ns simple-http-server
  (:require [org.httpkit.server :as http]
            [clojure.java.io :as io]
            [clojure.string :as string]))

; Dir paths
(def home (System/getProperty "user.home"))
(def path "/TEMP")
(def dir-path (str home path))

(defn folder-html [uri name]
 (str "<li><a href='" (str uri name) "'>" (str name "/") "</a> </li>"))

(defn file-html [uri name]
 (str "<li><a href='" (str uri name) "' download>" (str name) "</a> </li>"))
 
(defn dirs-to-string [uri file]
  (let [name (.getName file)
        new-uri (if (= uri "/") uri (str uri "/"))]
    (cond
      (.isDirectory file) (folder-html new-uri name)
      (.isFile file) (file-html new-uri name)
      :else "")))

(defn prepend-up-dir [uri]
  (if (= uri "/") nil
      (let [prev-folder (string/join "/" (pop (string/split uri #"/")))]
        (str "<li><a href='" (if (empty? prev-folder) "/" prev-folder) "'>..</a></li>"))))

(defn list-folders
  ([path] (list-folders "/" path))
  ([uri path]
    (->> (io/file path)
        (.listFiles)
        (map #(dirs-to-string uri %))
        (string/join)
        )))

(defn generate-html
  [title uri items]
  (let [title-html (str "<h1>" title "</h1>")
        uri-html  (str "<b>URI:</b>" uri)
        prev-dir (or (prepend-up-dir uri) "")
        contents (str "<hr/><ul>" prev-dir items "</ul><hr/>")]
     (str title-html uri-html contents)))

(defn contents [uri path]
  (let [folders (list-folders uri path)]
    (generate-html "Simple HTTP Server" uri folders)))

;; Server

(defn get-path [uri]
    (if (= uri "/") dir-path (str dir-path uri)))

(def error-response {:status 404 :body "404 Not Found"})

(defn file-download-response [file-path]
  {:status 200
   :headers {"Content-Type" "application/octet-stream"
             "Content-Disposition" (str "attachment; filename="(.getName file-path))}
   :body (io/input-stream file-path)})

(defn folder-html-response [uri path]
  {:status 200
   :headers {"Content-Type" "text/html"}
   :body (contents uri path)})

(defn handler [request]
  (let [uri (or (:uri request) "/")
        path (get-path uri)
        file-path (io/file path)]
    (if file-path
      (cond
        (.isFile file-path) (file-download-response file-path)
        (.isDirectory file-path) (folder-html-response uri path)
        :else error-response
        )
      error-response)))

(defonce server (atom nil))

(defn stop-server []
  (when-not (nil? @server)
    ;; graceful shutdown: wait 100ms for existing requests to be finished
    ;; :timeout is optional, when no timeout, stop immediately
    (@server :timeout 100)
    (reset! server nil)))

(defn -main [& args]
  (reset! server (http/run-server #'handler {:port 8080})))
