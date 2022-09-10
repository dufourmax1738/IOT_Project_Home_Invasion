import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Table(name = "sidedish")
@Setter
@Getter
@NoArgsConstructor
public class SideDish {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "sidedishid", unique = true)
    private Integer sideDishId;

    private String title;

    private double price;

    private String description;
}
