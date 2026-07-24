import * as fs from "fs";
import * as path from "path";
import type { Compilation, Compiler } from "webpack";

interface ConcatenatePluginOptions {
  source?: string;
  destination: string;
  name: string;
  ignore?: string[];
}

class ConcatenatePlugin {
  readonly source: string;
  readonly destination: string;
  readonly name: string;
  readonly ignore: string[];

  constructor(options: ConcatenatePluginOptions) {
    this.source = options.source ?? "./dist";
    this.destination = path.resolve(options.destination);
    this.name = options.name;
    this.ignore = options.ignore ?? [];
  }

  apply(compiler: Compiler): void {
    compiler.hooks.afterEmit.tapAsync(
      "ConcatenatePlugin",
      (_compilation: Compilation, callback: (error?: Error | null) => void) => {
        try {
          const sourceDir = path.resolve(this.source);
          const jsFiles = this.findJsFiles(sourceDir);

          if (jsFiles.length === 0) {
            console.warn("[ConcatenatePlugin] No JavaScript files found");
            callback();
            return;
          }

          const contents = jsFiles
            .map((file) => fs.readFileSync(file, "utf8"))
            .join("\n");

          fs.mkdirSync(this.destination, { recursive: true });
          fs.writeFileSync(path.join(this.destination, this.name), contents);
          callback();
        } catch (error) {
          callback(error as Error);
        }
      },
    );
  }

  private findJsFiles(dir: string): string[] {
    let results: string[] = [];

    for (const file of fs.readdirSync(dir)) {
      const filePath = path.join(dir, file);
      if (fs.statSync(filePath).isDirectory()) {
        results = results.concat(this.findJsFiles(filePath));
      } else if (
        path.extname(file) === ".js" &&
        !this.ignore.includes(file)
      ) {
        results.push(filePath);
      }
    }

    return results.sort();
  }
}

export default ConcatenatePlugin;
