Go Examples
-----------

{% from "dexy.jinja" import hl, ext with context -%}

The website for go is `golang.org <http://golang.org/>`__.

Here is some go code:

{{ hl(d['hello.go'], "go") }}

The `go` filter runs code through the `go run` command:

    {{ d['dexy.yaml|idio|t']['go'] | indent(4) }}

Here is the output, just what was printed to stdout::

    {{ d['hello.go|go'] | indent(4) }}

Here is another example:

{{ hl(d['rand.go'], "go") }}

And its output::

    {{ d['rand.go|go'] | indent(4) }}
