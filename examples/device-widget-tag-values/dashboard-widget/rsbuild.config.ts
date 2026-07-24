import {
  createModuleFederationConfig,
  pluginModuleFederation,
} from "@module-federation/rsbuild-plugin";
import { defineConfig } from "@rsbuild/core";
import { pluginReact } from "@rsbuild/plugin-react";

import SingleFileWidgetPlugin from "./SingleFileWidgetPlugin";

const moduleFederation = createModuleFederationConfig({
  name: "TagValuesWidget",
  remotes: {
    doover_admin: "doover_admin@[window.dooverAdminSite_remoteUrl]",
    customer_site: "customer_site@[window.dooverCustomerSite_remoteUrl]",
  },
  exposes: {
    "./TagValuesWidget": "./src/TagValuesWidget",
  },
  shared: {
    react: { singleton: true, requiredVersion: "^18.3.1", eager: true },
    "react-dom": { singleton: true, requiredVersion: "^18.3.1", eager: true },
    "react-router": { singleton: true, requiredVersion: false, eager: true },
    "doover-js": { singleton: true, requiredVersion: false, eager: true },
    "doover-js/react": { singleton: true, requiredVersion: false, eager: true },
    "@tanstack/react-query": { singleton: true, requiredVersion: false, eager: true },
  },
});

export default defineConfig({
  output: { injectStyles: true },
  performance: { chunkSplit: { strategy: "all-in-one" } },
  plugins: [pluginReact(), pluginModuleFederation(moduleFederation)],
  tools: {
    rspack: {
      plugins: [
        new SingleFileWidgetPlugin({
          source: "./dist",
          destination: "./assets",
          filename: "TagValuesWidget.js",
          ignore: ["main.js"],
        }),
      ],
    },
  },
});
