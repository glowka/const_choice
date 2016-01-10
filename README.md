EXAMPLE USAGE

```
package_types = Consts(
    BASIC=C({
        'id': 100,
        'price': 477,
        'label': 'standard'
    }),
    STANDARD=C(
        1003,
        price=477,
        label='standard'
    ),
    CUSTOM=C(
        id=3,
        price=977,
        label='custom'
    ),
    choice=lambda const: const.label
)

package_types.BASIC
# 100
package_types.basic
# <BASIC: 100 {'price': 477, 'label': 'standard'}>
package_types.basic.price
# 477
package_types.basic['price']
# 477
package_types.get_choices()
# ((100, 'standard'), (1003, 'standard'), (3, 'custom'))
```