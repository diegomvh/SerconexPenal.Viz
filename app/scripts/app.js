'use strict';

/**
 * @ngdoc overview
 * @name serconexPenalvizApp
 * @description
 * # serconexPenalvizApp
 *
 * Main module of the application.
 */
angular
  .module('serconexPenalvizApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
