import { defineConfig } from "vite";
import { resolve } from "path";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  base: "/static/", // this has to match STATIC_URL in settings.py
  resolve: {
    alias: {
      "@": resolve("./kahf_learning/static"),
    },
  },
  build: {
    manifest: "manifest.json",
    outDir: resolve(__dirname, "./kahf_learning/assets"),
    assetsDir: "django-assets",
    rollupOptions: {
      input: {
        test: resolve(__dirname, "./kahf_learning/static/js/main.js"),
      },
    },
  },
  plugins: [tailwindcss()],
});
