public interface SideDishService {

    public List<SideDishResponseModel> findAllSideDishes();
    public SideDishResponseModel findSideDishById(Integer sideDishId);
    public SideDishResponseModel newSideDish(SideDishRequestModel newSideDish);
}