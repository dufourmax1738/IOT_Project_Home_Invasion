import org.springframework.data.repository.CrudRepository;

public interface MainDishRepository extends CrudRepository<MainDish,Integer>{
    MainDish findTitleByMainDishId(Integer mainDishId);
    boolean existsTitleByMainDishId(Integer mainDishId);
}