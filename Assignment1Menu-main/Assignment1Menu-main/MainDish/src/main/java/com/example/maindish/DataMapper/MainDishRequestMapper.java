@Mapper(componentModel="spring")
public Interface MainDishRequestMapper(){
@Mappings({
        @Mapping(target = "id", ignore = true),
        @Mapping(target = "mainDishId", ignore = true)
})
        MainDish requestModelToEntity(MainDishRequestModel model);
                }