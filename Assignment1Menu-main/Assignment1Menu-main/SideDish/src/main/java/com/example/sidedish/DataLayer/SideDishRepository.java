import org.springframework.data.repository.CrudRepository;

public interface SideDishRepository extends CrudRepository<SideDish,Integer>{
    SideDish findTitleBySideDishId(Integer sideDishId);
    boolean existsTitleBySideDishId(Integer sideDishId);
}