 @Mapper(componentModel="spring")
 public Interface SideDishRequestMapper(){
    @Mappings({
           @Mapping(target = "id", ignore = true),
           @Mapping(target = "sideDishId", ignore = true)
        })
        SideDish requestModelToEntity(SideDishRequestModel model);
 }