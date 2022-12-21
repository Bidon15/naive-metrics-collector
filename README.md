Motivation
---

While testground is still in progress with out-of-the-box metrics and logs collection, this is the scripts to just have
at least some info on test pods

### What are these scripts doing

1. `main.py` -> calling `kubectl exec` to gather metrics.json from app validators
2.  Manual(will be done later with regexp): you need to manually add commas into json obj
3. `read.py` -> prepping the broken json to a list type
4. `transform.py` -> get the final json obj
5. `final.py` -> insights on low/high/average

### Artifacts

v1 and v2 dirs contains .json files taken from k8s pods