Bash Examples
-------------

Here is a simple bash script::

    {{ d['script.sh'] | indent(4) }}

The bash filter runs scripts in bash and returns the output::

    {{ d['dexy.yaml|idio']['bash'] | indent(4) }}

Here is the output::

    {{ d['script.sh|bash'] | indent(4) }}

The sh filter runs scripts in sh (dash) and returns the output::

    {{ d['dexy.yaml|idio']['sh'] | indent(4) }}

Here is the output::

    {{ d['script.sh|sh'] | indent(4) }}

The shint filter runs scripts in a bash REPL, so you can see both input and output::

    {{ d['dexy.yaml|idio']['shint'] | indent(4) }}

Here is the output::

    {{ d['script.sh|shint'] | indent(4) }}

