# overlay-risk

Simple on-chain risk metrics to inform our choices for per-market funding constants.


## Assumptions

We sample data from on-chain oracles and assume the underlying feed exhibits [Geometric Brownian motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion) of the form

```
P_j = P_0 * e**(mu * j * T + sig * W(j*T))
```

where `W(j*T)` is a [Wiener process](https://en.wikipedia.org/wiki/Wiener_process), `j` is an `int` for the number of update intervals that occur after the initial feed value of `P_0`, and `T` is the update interval of the respective feed (e.g. sliding window oracles currently maintained by [Keep3r Network](https://github.com/keep3r-network/keep3r.network) have `T = periodSize = 30 min`).


## Why?

We need some way to assess the [risk to the system](https://github.com/overlay-market/OIPs/blob/master/notes/note-4.md). A good approach is to model the underlying feed value as being driven by a stochastic process, which allows us to estimate expected values to be paid out by the protocol for an imbalance in positions on a market in addition to the "VaR" for passive OVL holders, who act as the counterparty to all unbalanced trades.

Calculation of our per-market risk metrics requires estimating distributional parameters for the underlying stochastic model. This repo aims to provide easy to access views on-chain for those parameters (i.e. maximum likelihood estimates for `mu` and `sig` above).


## Requirements

To run the project you need:

- Python >=3.7.2 local development environment
- [Brownie](https://github.com/eth-brownie/brownie) local environment setup
- Set env variables for [Etherscan API](https://etherscan.io/apis) and [Infura](https://eth-brownie.readthedocs.io/en/stable/network-management.html?highlight=infura%20environment#using-infura): `ETHERSCAN_TOKEN` and `WEB3_INFURA_PROJECT_ID`
- Local Ganache environment installed
- [InfluxDB](https://www.influxdata.com/) set up with local environment variables: `INFLUXDB_TOKEN`, `INFLUXDB_ORG`, `INFLUXDB_URL`


## Installation

Using [Poetry](https://github.com/python-poetry/poetry) for dependencies. Install with `pipx`

```
pipx install poetry
```

Clone the repo, then

```
poetry install
```

within the local dir.


## Scripts

To run, for example, the script to ingest stat parameters for historical risk analysis, do

```
poetry shell
brownie run influx_kv1o --network mainnet
```
