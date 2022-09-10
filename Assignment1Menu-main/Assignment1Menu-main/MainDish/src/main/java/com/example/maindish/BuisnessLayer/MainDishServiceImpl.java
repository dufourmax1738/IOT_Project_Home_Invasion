@Service
public class MainDishServiceImpl implements MainDishService {

    final private MainDishRepository mdRep;
    final private MainDishResponseMapper mdRepM;
    final private MainDishRequestMapper mdReqM;

    public MainDishServiceImpl(
            MainDishRepository mainDishRepository,
            MainDishResponseMapper mainDishResponseMapper,
            MainDishRequestMapper mainDishRequestMapper){
        this.mdRep = mainDishRepository;
        this.mdRepM = mainDishResponseMapper;
        this.mdReqM = mainDishRequestMapper;
    }

    @Override
    public List<MainDishResponseModel> findAllMainDishes() {

        List<MainDish> mainDishList = (List<MainDish>)mdRep.findAll();
        List<MainDishResponseModel> mainDishList =
                mdRepM.entityListToResponseModel(gameList);

        return mainDishList;
    }

    @Override
    public MainDishResponseModel findMainDishById(Integer mainDishId) {
        MainDish mainDish = mdRep.findTitleByMainDishId(gameId);
        mdRepM mainDishModel = mdRepM.entityToResponseModel(mainDish);

        return mainDishModel;
    }

    @Override
    public MainDishResponseModel newMainDish(MainDishRequestModel newMainDish) {

        MainDish mainDishEntity = mdReqM.requestModelToEntity(newMainDish);

        String shortIdString = RandomStringUtils.randomNumeric(LENGTH_ID);

        Integer shortId = Integer.valueOf(shortIdString);

        while(mdRep.findTitleByMainDishId(shortId) != null) {

            shortIdString = RandomStringUtils.randomNumeric(LENGTH_ID);

            shortId = Integer.valueOf(shortIdString);
        }

        mainDishEntity.setMainDishId(shortId);

        MainDish createdMainDish = mdRep.save(mainDishEntity);

        MainDishResponseModel responseModel =
                mdRepM.entityToResponseModel(createdMainDish);

        return responseModel;
    }
}