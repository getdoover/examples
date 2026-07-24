import { mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { basename, join, resolve } from "node:path";

const sourceDirectory = resolve("dist");
const outputDirectory = resolve("assets");
const outputFile = join(outputDirectory, "FleetOverviewDashboardWidget.js");

async function findJavaScriptFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = await Promise.all(
    entries.map(async (entry) => {
      const path = join(directory, entry.name);
      if (entry.isDirectory()) return findJavaScriptFiles(path);
      if (entry.isFile() && entry.name.endsWith(".js")) return [path];
      return [];
    }),
  );

  return files.flat().filter((path) => basename(path) !== "main.js").sort();
}

const files = await findJavaScriptFiles(sourceDirectory);
if (files.length === 0) {
  throw new Error("Rsbuild produced no JavaScript files");
}

const contents = await Promise.all(files.map((file) => readFile(file, "utf8")));
await rm(outputDirectory, { recursive: true, force: true });
await mkdir(outputDirectory, { recursive: true });
await writeFile(outputFile, `${contents.join("\n")}\n`);

console.log(`Built ${outputFile} from ${files.length} chunks`);
