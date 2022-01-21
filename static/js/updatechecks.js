var fields = $(".fields");
fields.change(function() {
  Array.prototype.reduce.call(fields, function(prev, curr) {
    curr.disabled = !prev.checked || prev.disabled;

    /*
      If you want to uncheck remianing use this instead of above line:
      curr.checked = prev.checked ? curr.checked : false;
      curr.disabled = !prev.checked;
    */
    return curr;
  });
});

fields.change();