@RestController
@RequestMapping("/api")
public class SideDishController{

    @Autowired
    private SideDishService sdS;

    @GetMapping("/sidedish")
    public List<SideDishResponseModel> getAllSideDishes(){
        List<SideDishResponseModel> sideDish = sdS.findAllSideDishes();

        return sideDish;
    }

    @GetMapping("/sidedish/{sideDishId}")
    public ResponseEntity<SideDishResponseModel> getSideDishById(@PathVariable Integer gameId){
        SideDishResponseModel sideDish = sdS.findSideDishById(sideDishId);

        return ResponseEntity.status(HttpStatus.CREATED).body(sideDish);
    }

    @PostMapping("/sidedish")
    public ResponseEntity<SideDishResponseModel> createdSideDish(@RequestBody SideDishRequestModel newSideDish){
        SideDishResponseModel sideDish = sdS.newSideDish(newSideDish);

        return ResponseEntity.status(HttpStatus.CREATED).body(sideDish);
    }
}