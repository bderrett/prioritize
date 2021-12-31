# Prioritizer

This is a tiny Python script to help you determine what to do next. You supply a list of tasks, and it asks you to make pairwise comparisons between tasks until the most important task is identified. The comparisons are then stored in the task file.

## Usage

Add tasks to a file (`mytasks.json`):

```json
{
  "names": ["buy groceries", "fix dripping tap", "do laundry"],
  "preferences": []
}
```

Then run the script:

```shell
> python prioritize.py mytasks.json
Is buy groceries more important than fix dripping tap? [y/n]
n
Is do laundry more important than fix dripping tap? [y/n]
y
Your first task is: do laundry. Go!
```

Afterwards your `mytasks.json` file contains:

```json
{
  "names": ["buy groceries", "fix dripping tap", "do laundry"],
  "preferences": [
    {
      "better": "fix dripping tap",
      "worse": "buy groceries"
    },
    {
      "better": "do laundry",
      "worse": "fix dripping tap"
    }
  ]
}
```

If you run the script again, it remembers your previous comparisons:

```shell
> python prioritize.py mytasks.json
Your first task is: do laundry. Go!
```

To add or remove tasks, edit `mytasks.json`.

## Dependency

`pydantic`

## Why

There's an infinitude of things we could do: errands to run, books to read, videos to watch and comments to write. This tool is meant to reduce load on your attentional system in situations in which

- speed matters,
- it's not obvious what to do next,
- and there are more options than you can hold in short term memory.

I run a start-up, so there are always new things coming up that could be done. When one does, I put it on my task list and return to what I was doing. When I'm done, I run the script again. Answering the questions only takes a few seconds. I find the script invaluable, and maybe you will too.

(Please let me know if you're aware of other similar tools. I'm particularly interested in finding a similar tool that works for teams.)
