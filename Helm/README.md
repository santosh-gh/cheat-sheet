# Helm Chart Structure

  mychart
  |-- Chart.yaml
  |-- charts
  |-- templates
  |   |-- NOTES.txt
  |   |-- _helpers.tpl
  |   |-- deployment.yaml
  |   |-- ingress.yaml
  |   |-- service.yaml
  |-- values.yaml

  templates/ contains the templated kubernetes objetcs

  values.yaml contains the default values of the chart

  Chart.yaml contains a description of the chart

  charts/ directory is used to define sub-charts

  .helmignore to list the files not included in the helm chart package
  

# What is _helpers TPL in helm?

  In Helm, _helpers.tpl is a special file used for defining reusable templates and utility functions within a Helm chart. 
  It is a common practice to create this file to store complex or repetitive template logic that can be shared among 
  different templates in the chart. By placing shared code in _helpers.tpl, you can avoid duplicating the same logic 
  in multiple templates and keep your chart more organized and maintainable.

  Typically, _helpers.tpl is placed in the templates directory alongside other YAML or Go template files. The name of 
  the file usually starts with an underscore (_) to indicate that it is a helper file and not intended to be rendered 
  directly as a Kubernetes manifest.

  Inside _helpers.tpl, you can define custom template functions, pipelines, or variables that can be used in other templates. 
  These functions and variables can assist with tasks like generating labels, annotations, handling complex configurations, 
  or performing computations based on chart values.

  Here's a simple example of what _helpers.tpl might look like:


  File: _helpers.tpl
  {{/* Define a custom function to generate a label */}}
  {{- define "mychart.labels" -}}
    app: {{ default .Values.appName "my-app" }}
    release: {{ .Release.Name }}
  {{- end }}
  You can then use this custom label generation function in other templates like this:


  File: deployment.yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: {{ .Release.Name }}
    labels:
      {{ include "mychart.labels" . | nindent 4 }}
  spec:
    replicas: {{ .Values.replicas }}
    # ...
  This way, you keep your templates clean, modular, and easy to manage.

  Keep in mind that the specific naming or usage conventions for _helpers.tpl might vary based on the chart author's 
  preference, but the general idea of using it for reusable logic remains the same. I recommend checking the official 
  Helm documentation and any documentation or examples specific to the chart you are working with for the most up-to-date 
  and accurate information.

