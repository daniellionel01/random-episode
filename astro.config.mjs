import { defineConfig } from "astro/config";
import preact from "@astrojs/preact"

// https://astro.build/config
export default defineConfig({
  site: "https://daniellionel01.github.io",
  base: "/random-episode",
  integrations: [preact()]
});
