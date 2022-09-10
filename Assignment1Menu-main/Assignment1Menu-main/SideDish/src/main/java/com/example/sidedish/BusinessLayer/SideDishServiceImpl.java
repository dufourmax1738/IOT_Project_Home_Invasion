@Service
public class SideDishServiceImpl implements SideDishService {

    final private SideDishRepository sdRep;
    final private SideDishResponseMapper sdRepM;
    final private SideDishRequestMapper sdReqM;

    public SideDishServiceImpl(
            SideDishRepository sideDishRepository,
            SideDishResponseMapper sideDishResponseMapper,
            SideDishRequestMapper sideDishRequestMapper){
        this.sdRep = sideDishRepository;
        this.sdRepM = sideDishResponseMapper;
        this.sdReqM = sideDishRequestMapper;
    }

    @Override
    public List<SideDishResponseModel> findAllSideDishes() {

        List<SideDish> sideDishList = (List<SideDish>)sdRep.findAll();
        List<SideDishResponseModel> sideDishList =
                sdRepM.entityListToResponseModel(gameList);

        return sideDishList;
    }

    @Override
    public SideDishResponseModel findSideDishById(Integer sideDishId) {
        SideDish sideDish = sdRep.findTitleBySideDishId(gameId);
        sdRepM sideDishModel = sdRepM.entityToResponseModel(sideDish);

        return sideDishModel;
    }

    @Override
    public SideDishResponseModel newSideDish(SideDishRequestModel newSideDish) {

        SideDish sideDishEntity = sdReqM.requestModelToEntity(newSideDish);

        String shortIdString = RandomStringUtils.randomNumeric(LENGTH_ID);

        Integer shortId = Integer.valueOf(shortIdString);

        while(sdRep.findTitleBySideDishId(shortId) != null) {

            shortIdString = RandomStringUtils.randomNumeric(LENGTH_ID);

            shortId = Integer.valueOf(shortIdString);
        }

        sideDishEntity.setSideDishId(shortId);

        SideDish createdSideDish = sdRep.save(sideDishEntity);

        SideDishResponseModel responseModel =
                sdRepM.entityToResponseModel(createdSideDish);

        return responseModel;
    }
}