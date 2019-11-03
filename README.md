# openfaas-inceptionfeed

An [openfaas](https://www.openfaas.com/) function that takes an array of image URLs, and calls [inception](https://github.com/faas-and-furious/inception-function) on them.

```bash
echo '["http://scottleedavis.com/assets/img/scott.jpeg"]' | faas-cli invoke openfaas-inceptionfeed | jq

[
  {
    "url": "http://scottleedavis.com/assets/img/scott.jpeg",
    "inception": [
      {
        "score": 0.44882360100746155,
        "name": "suit"
      },
      {
        "score": 0.06006264314055443,
        "name": "bassoon"
      },
      {
        "score": 0.03918169438838959,
        "name": "bulletproof vest"
      },
      {
        "score": 0.033128831535577774,
        "name": "jersey"
      },
      {
        "score": 0.030749458819627762,
        "name": "oboe"
      },
      {
        "score": 0.02307302877306938,
        "name": "sax"
      },
      {
        "score": 0.016684917733073235,
        "name": "Windsor tie"
      },
      {
        "score": 0.012078914791345596,
        "name": "trench coat"
      },
      {
        "score": 0.011429266072809696,
        "name": "bow tie"
      },
      {
        "score": 0.009498999454081059,
        "name": "notebook"
      }
    ]
  }
]
```