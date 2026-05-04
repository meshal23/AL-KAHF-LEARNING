import "@/css/main.css";
import "flowbite";
import htmx from "htmx.org";
import Alpine from "alpinejs";

// Make HTMX globally accessible
window.htmx = htmx;
window.Alpine = Alpine;

Alpine.start();
