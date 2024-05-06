# Daily Standup Assistant

An automated assistant to summarise the work done each day for a DevOps Engineer

## Setup

### Install requirements

This is simple! Just run

```
pip install -r requirements.txt
```

### Ollama

You need to download & setup [ollama](https://ollama.com/) to run a local LLM.

Just download the installer from the website and then pull the model you want to run. Example:

```
ollama pull llama3
ollama run llama3
```

### Commit hooks

You'll need to copy the file `post-commit` into any repository that you want to be included. 

This file should be located in $repo_dir/.git/hooks

**Don't forget to chmod +x the file, if not you won't be able to use it.**

### Environment variables

You'll need to set the `COMMITS_DIRECTORY` environment variable with a directory which will contain the result of the commits and the summary.


### Crontab setup

If you want a recurrent execution, you can run `crontab -e` which will open the crontab file.

An example regex would be:

```
0 9 * * MON-FRI python /your-working-dir/daily-standup-assistant/main.py
```

If you want other cron, you can always use [crontab guru](https://crontab.guru/) 
