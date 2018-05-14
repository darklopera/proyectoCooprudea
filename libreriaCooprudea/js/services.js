angular.module('app.services', [])

.factory('BlankFactory', [function(){

}])

.service('BlankService', [function(){

}])

.service('CategoriasExistentes', [function(){
    
    var data = {};
    return{
      data
    };

}])

.service('TiposDeBusqueda', [function(){
    
    var data = [{id:"1",
               tipo:"Titulo"},
               {id:"2",
               tipo:"Autor"}];
    return{
      data
    };

}])

.service('EstadoTiposBusqueda', [function(){
    
    var data = {};
    return{
      data
    };

}])

;