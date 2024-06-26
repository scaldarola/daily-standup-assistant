# Daily Standup Assistant

An automated assistant to summarise the work done each day for a DevOps Engineer

## Usage

You can run the script one-shot by just executing the `main.py` file, or [use a cronjob](#crontab-setup).

The summarised output will be printed, and also saved in a file in `$COMMITS_DIRECTORY/results/$today.txt`

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

## To Do
* Do some code cleaning
* Add a [Model file](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)
* Integrate with Calendar app
* Integrate with Email
* Fine tune the model and the prompt