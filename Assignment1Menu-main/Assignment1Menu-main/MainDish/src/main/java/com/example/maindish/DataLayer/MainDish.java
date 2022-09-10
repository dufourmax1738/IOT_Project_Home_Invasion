import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Table(name = "maindish")
@Setter
@Getter
@NoArgsConstructor
public class MainDish {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "maindishid", unique = true)
    private Integer mainDishId;

    private String title;

    private double price;

    private String description;
}
