'use strict';

/**
 * @ngdoc service
 * @name serconexPenalvizApp.d3Service
 * @description
 * # d3Service
 * Factory in the serconexPenalvizApp.
 */
angular.module('serconexPenalvizApp')
  .factory('d3Service', function () {
    // Service logic
    // ...

    var meaningOfLife = 42;

    // Public API here
    return {
      someMethod: function () {
        return meaningOfLife;
      }
    };
  });
