(function() {
  packages = {

    // Lazily construct the package hierarchy from class names.
    root: function(classes) {
      var root = {name: "", children: [], parent:null}
      var map = {};
      
      function find(name, data) {
        data.parent = root;
        data.key = name;
        map[name] = data;
        root.children.push(map[name]);
        return data;
      }

      classes.forEach(function(d) {
        find(d.name, d);
      });

      return root;
    },

    // Return a list of imports for the given array of nodes.
    imports: function(nodes) {
      var map={}, imports = [];

      // Compute a map from name to node.
      nodes.forEach(function(d) {
        map[d.name] = d;
      });

      // For each import, construct a link from the source to target node.
      nodes.forEach(function(d) {
          if (d.habilitaciones) d.habilitaciones.forEach(function(h) {
            if (map[h])
              imports.push({source: map[d.name], target: map[h]});
          });
      });

      return imports;
    }

  };
})();
