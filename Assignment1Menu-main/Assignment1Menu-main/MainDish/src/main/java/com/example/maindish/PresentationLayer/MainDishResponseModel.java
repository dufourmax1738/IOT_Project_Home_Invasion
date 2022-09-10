@NoArgsConstructor
@Getter
@Setter
public class MainDishResponseModel extends RepresentationalModel<MainDishResponseModel>{

    public Integer mainDishId;

    public String title;

    public double price;

    public String description;

}