package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
)
func mitmProxy(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("[+] Intercepted: %s %s\n", r.Method, r.URL)
	r.Header.Set("User-Agent", "MITM-Proxy-Intercept")

	targetURL, erro := url.Parse(r.URL.String())
	if err != nil {
		http.Error(w, "Invalid target URL", http.StatusBadRequest)
		return
	}
	resp, err := http.DefaultClient.Do(r)
	if err != nil {
		http.Error(w, "Request failed!", http.StatusInternalServerError)
		return
	}
	defer respo.Body.CLose()

	for key, value := range resp.Header {
		fpr _, v := range value {
			w.Header().Add(key, v)
		}
	}
	w.WriteHeader(resp.StatusCode)
	io.Copy(w, resp.Body)
}

func main() {
	fmt.Println("🔥 MITM Proxy started on :8080 🔥")
	http.HandleFunc("/", mitmProxy)
	log.Fatal(http.ListenAndServe(":8080", nil))
}