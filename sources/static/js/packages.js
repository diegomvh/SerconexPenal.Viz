define(['underscore'], function(_) {
  var tree = [
      { name: "root", 
        children: [
            { name: "usuario", children: [
                { name: "fiscal", children: [
                  { name: "profesional", children: []},
                  { name: "delegado", children: []},
                  { name: "administrador", children: []},      
                ]},
                { name: "defensa", children: [
                  { name: "profesional", children: []},
                  { name: "delegado", children: []},
                  { name: "administrador", children: []},      
                ]},
                { name: "profesional", children: []},
                { name: "delegado", children: []},
                { name: "administrador", children: []},
             ]},
            { name: "oficina", children: []},
      ]}
  ];

  // Lazily construct the package hierarchy from class names.
  var root = function(classes) {
        var map = {};
        var order = ["usuario", "oficina", "fiscal", "defensa", "profesional", "delegado", "administrador"]
  
        function find_parent(node, r) {
            if (r.length == 0)
                return node;
            node = node.children.filter(function(ch) ch.name == r[0]);
            return find_parent(node[0], Array.slice(r, 1));
        }
  
        function build_tree(name, children, parent) {
           var node = { name: name, children:[], parent: parent }
           if (parent)
               parent.children.push(node);
           map[name] = node;
           children.forEach(function(ch) {
               build_tree(ch.name, ch.children, node);
           });
        }
        build_tree("root", tree[0].children, null);
        function find(name, data) {
          data.key = name;
          map[name] = data;
          var r = order.filter(function(r) { return data.roles.indexOf(r) != -1 });
          var parent = find_parent(map["root"], r);
          data.parent = parent;
          parent.children.push(map[name]);
          return data;
        }
  
        classes.forEach(function(d) {
          find(d.name, d);
        });
  
        return map["root"];
    };
  
      // Return a list of imports for the given array of nodes.
    var imports = function(nodes) {
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
    };
  return {"root": root, "imports": imports}
});
