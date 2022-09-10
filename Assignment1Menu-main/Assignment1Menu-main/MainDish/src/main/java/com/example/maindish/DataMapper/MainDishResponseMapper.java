@Mapper(componentModel="spring")
public Interface MainDishResponseMapper(){

        MainDishResponseModel entityToResponseModel(MainDish entity);
        List<MainDishResponseModel> entityListToResponseModel(List<MainDish> mainDish);

        }