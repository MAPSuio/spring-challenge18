# MIU

The MIU-system i a simple one. You are given a single string `MI` in your
possession, from which new strings of the `MIU` system may be derived. The
system is governed by the following rules:

1. `xI` → `xIU`

    Any string ending with `I` may be extended with a `U`.

2. `Mx` → `Mxx`

    For any string starting with `M`, the string may be extended with the
    entire content of what comes after `M`.

3. `xIIIy` → `xUy`

    Whenever `III` appears in a string, it may be replaced with `U`.

4. `xUUy` → `xy`

    Whenever `UU` appears in a string, it may be omitted.

From `MI`, both `MIU` and `MII` may be derived in one step.

The string `MUIU` may be derived from `MI` in four steps:

  * `MI`
  * `MII` by (2)
  * `MIIII` by (2)
  * `MIIIIU` by (1)
  * `MUIU` by (3)

In [this](./mius) file you'll find a hundred strings derivable from `MI` in the
`MIU`-system. For each string, we are interested in the minimum number of rules
one have to apply to reach it from `MI`. Provide your answer as a single
number, which corresponds to the sum of rules needed to produce each string.
