## Pre-deployment Checks

1. **Verify current branch and status:**
   ```bash
   git status
   git branch --show-current
````

2. __Run tests to ensure everything passes:__

   ```bash
   npm test
   ```

3. __Check for any linting issues:__

   ```bash
   npm run lint
   ```

4. __Ask user for confirmation before proceeding:__

   ```xml
   <ask_followup_question>
   <question>All pre-deployment checks passed. Ready to proceed with deployment to production?</question>
   <options>["Yes, proceed with deployment", "No, let me review first", "Run additional checks"]</options>
   </ask_followup_question>
