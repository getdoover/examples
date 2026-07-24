import * as fs from "node:fs";
import * as path from "node:path";

import type { Compiler } from "@rspack/core";

interface SingleFileWidgetPluginOptions {
  source?: string;
  destination: string;
  filename: string;
  ignore?: string[];
}

/**
 * Doover expects a widget at one asset path. Module Federation emits several
 * JavaScript files, so concatenate those files deterministically after build.
 */
class SingleFileWidgetPlugin {
  private readonly source: string;
  private readonly destination: string;
  private readonly filename: string;
  private readonly ignore: string[];

  constructor(options: SingleFileWidgetPluginOptions) {
    this.source = options.source ?? "./dist";
    this.destination = path.resolve(options.destination);
    this.filename = options.filename;
    this.ignore = options.ignore ?? [];
  }

  apply(compiler: Compiler): void {
    compiler.hooks.afterEmit.tapAsync(
      "SingleFileWidgetPlugin",
      (_compilation, callback) => {
        try {
          const files = this.findJavaScriptFiles(path.resolve(this.source));
          const contents = files.map((file) => fs.readFileSync(file, "utf8")).join("\n");

          fs.mkdirSync(this.destination, { recursive: true });
          fs.writeFileSync(path.join(this.destination, this.filename), contents);
          callback();
        } catch (error) {
          callback(error as Error);
        }
      },
    );
  }

  private findJavaScriptFiles(directory: string): string[] {
    return fs
      .readdirSync(directory, { withFileTypes: true })
      .flatMap((entry) => {
        const entryPath = path.join(directory, entry.name);
        return entry.isDirectory()
          ? this.findJavaScriptFiles(entryPath)
          : path.extname(entry.name) === ".js" && !this.ignore.includes(entry.name)
            ? [entryPath]
            : [];
      })
      .sort();
  }
}

export default SingleFileWidgetPlugin;
