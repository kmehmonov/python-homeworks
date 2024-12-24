
class Vector:
    """
    Define n dimentional vector
    """
    def __init__(self, *args: float) -> None:
        if len(args) == 0:
            raise ValueError("A vector must have at least one component.")      
        self.dimension: int = len(args) 
        self.coordinates: tuple = args
    
    def __repr__(self) -> str:
        return f"Vector{self.coordinates}"
    
    def __getitem__(self, index):
        return self.coordinates[index]

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector): 
            raise TypeError("Can only add another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vector dimensions do not match for addition.")
        return Vector(*(i + j for i, j in zip(self.coordinates, other.coordinates)))

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector.")
        if self.dimension != other.dimension:
             raise ValueError("Vector dimensions do not match for subtraction.")
        return Vector(*(i - j for i, j in zip(self.coordinates, other.coordinates)))

    def __mul__(self, scalar: float) -> "Vector":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar")
        return Vector(*(i * scalar for i in self.coordinates))
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def dot_product(self, other: "Vector") -> float:
        if not isinstance(other, Vector):
            raise TypeError("Can only dot another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vector dimensions do not match for dot product.")
        return sum(i * j for i, j in zip(self.coordinates, other.coordinates))
    
    def get_magnitude(self) -> float:
        """
        Get the magnitude of the vector. 
        """
        return sum(i**2 for i in self.coordinates)**0.5

    def get_normalized(self) -> "Vector":
        """
        Get the normalized vector. 
        """
        magnitude = self.get_magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(i/magnitude for i in self.coordinates))
    

vector1 = Vector(1, 2, 3, 4)
vector2 = Vector(1, 2, 3, 0)
print("vector1:", vector1)
print("vector2:", vector2)
print("indexing:", vector1[0])
print("addition:", vector1 + vector2)
print("subtraction:", vector1 + vector2)
print("scalar multiplcation:", vector1*5)
print("scalar multiplcation:", 5*vector1)
print("dot product:", vector1.dot_product(vector2))
print("magnitude:", vector1.get_magnitude())
print("normalized:", vector1.get_normalized())






