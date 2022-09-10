public interface MainDishService {

    public List<MainDishResponseModel> findAllMainDishes();
    public MainDishResponseModel findMainDishById(Integer mainDishId);
    public MainDishResponseModel newMainDish(MainDishRequestModel newMainDish);