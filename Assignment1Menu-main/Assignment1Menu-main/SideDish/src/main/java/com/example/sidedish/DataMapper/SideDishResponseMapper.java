@Mapper(componentModel="spring")
public Interface SideDishResponseMapper(){

        SideDishResponseModel entityToResponseModel(SideDish entity);
        List<SideDishResponseModel> entityListToResponseModel(List<SideDish> sideDish);

}