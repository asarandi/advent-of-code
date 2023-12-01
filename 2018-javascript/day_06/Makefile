run: script.js
	/usr/bin/env node $<

script.js: script.ts 
	/usr/bin/env npx tsc $<

format:
	/usr/bin/env npx prettier -w script.ts
