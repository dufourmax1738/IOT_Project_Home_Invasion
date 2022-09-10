@RestController
@RequestMapping("/api")
public class MainDishController{

    @Autowired
    private MainDishService mdS;

    @GetMapping("/maindish")
    public List<MainDishResponseModel> getAllMainDishes(){
        List<MainDishResponseModel> mainDish = mdS.findAllMainDishes();

        return mainDish;
    }

    @GetMapping("/maindish/{mainDishId}")
    public ResponseEntity<MainDishResponseModel> getMainDishById(@PathVariable Integer gameId){
        MainDishResponseModel mainDish = mdS.findMainDishById(mainDishId);

        return ResponseEntity.status(HttpStatus.CREATED).body(mainDish);
    }

    @PostMapping("/maindish")
    public ResponseEntity<MainDishResponseModel> createdMainDish(@RequestBody MainDishRequestModel newMainDish){
        MainDishResponseModel mainDish = mdS.newMainDish(newMainDish);

        return ResponseEntity.status(HttpStatus.CREATED).body(mainDish);
    }
}