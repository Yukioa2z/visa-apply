#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");
const readline = require("readline");

const skillName = "visa-apply";
const packageRoot = path.resolve(__dirname, "..");
const sourceDir = path.join(packageRoot, "skill");

// Known agents and the skills directory each one scans.
const AGENTS = [
  { label: "Claude Code", dir: "~/.claude/skills" },
  { label: "Codex", dir: "~/.codex/skills" },
];

function usage() {
  const lines = AGENTS.map(
    (a) => `  ${a.label.padEnd(13)} npx @yukioa2z/visa-apply -- --dest ${a.dir}`
  ).join("\n");
  console.log(`Install ${skillName}

Pick your agent's skills directory with --dest:
${lines}
  Other agent   npx @yukioa2z/visa-apply -- --dest <your agent's skills dir>

Run with no --dest in a terminal to choose interactively.

Options:
  --dest <path>   Skill root directory.
  --dry-run       Print the destination without copying files.
  --help          Show this help message.
`);
}

function expandHome(value) {
  if (!value) return value;
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function readOption(name) {
  const args = process.argv.slice(2);
  const index = args.indexOf(name);
  if (index === -1) return undefined;
  return args[index + 1];
}

function install(destRoot, dryRun) {
  const destDir = path.join(destRoot, skillName);
  if (dryRun) {
    console.log(destDir);
    return;
  }
  fs.mkdirSync(destRoot, { recursive: true });
  fs.rmSync(destDir, { recursive: true, force: true });
  fs.cpSync(sourceDir, destDir, { recursive: true });
  console.log(`Installed ${skillName} to ${destDir}`);
  console.log(
    `Try: Use $${skillName} to check your visa need and prepare an application dossier.`
  );
}

function promptAgent() {
  return new Promise((resolve) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    console.log("Which agent are you installing for?\n");
    AGENTS.forEach((a, i) => console.log(`  ${i + 1}) ${a.label}  (${a.dir})`));
    console.log(`  ${AGENTS.length + 1}) Other  (enter a path)\n`);
    rl.question("Choice: ", (answer) => {
      rl.close();
      const n = parseInt(answer.trim(), 10);
      if (n >= 1 && n <= AGENTS.length) {
        resolve(AGENTS[n - 1].dir);
      } else if (n === AGENTS.length + 1) {
        const rl2 = readline.createInterface({ input: process.stdin, output: process.stdout });
        rl2.question("Skills directory path: ", (p) => {
          rl2.close();
          resolve(p.trim() || null);
        });
      } else {
        resolve(null);
      }
    });
  });
}

async function main() {
  const args = process.argv.slice(2);
  if (args.includes("--help") || args.includes("-h")) {
    usage();
    return;
  }
  if (!fs.existsSync(sourceDir)) {
    console.error(`Skill source not found: ${sourceDir}`);
    process.exitCode = 1;
    return;
  }

  const dryRun = args.includes("--dry-run");
  let dest = readOption("--dest");

  if (!dest) {
    // No target given. Ask interactively when attached to a terminal;
    // otherwise (agent/CI) print guidance and exit without guessing.
    if (process.stdin.isTTY && process.stdout.isTTY) {
      dest = await promptAgent();
    }
    if (!dest) {
      console.error("No skills directory chosen.\n");
      usage();
      process.exitCode = 1;
      return;
    }
  }

  install(path.resolve(expandHome(dest)), dryRun);
}

main();
