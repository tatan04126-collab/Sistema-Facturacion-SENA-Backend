from sqlalchemy import Column, Integer, String, Date
from src.models import Base


class Inventories(Base):
    __tablename__ = 'Inventories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=True)
    Brand = Column(String(45), nullable=True)
    Category = Column(String(45), nullable=True)
    UnitOfMeasure = Column(String(45), nullable=True)
    IVA_Percentage = Column(Integer, nullable=True)
    StockQuantity = Column(Integer, nullable=True)
    UnitValue = Column(Integer, nullable=True)
    DueDate = Column(Date, nullable=True)
    EntryDate = Column(Date, nullable=True)
    Category_id = Column(Integer, nullable=True)

    def __init__(self, name, description=None, Brand=None, Category=None, UnitOfMeasure=None, IVA_Percentage=None, StockQuantity=None, UnitValue=None, DueDate=None, EntryDate=None, Category_id=None):
        self.name = name
        self.description = description
        self.Brand = Brand
        self.Category = Category
        self.UnitOfMeasure = UnitOfMeasure
        self.IVA_Percentage = IVA_Percentage
        self.StockQuantity = StockQuantity
        self.UnitValue = UnitValue
        self.DueDate = DueDate
        self.EntryDate = EntryDate
        self.Category_id = Category_id

    def __repr__(self):
        return f"<inventory(id={self.id}, name='{self.name}', description='{self.description}', Brand='{self.Brand}', Category='{self.Category}', UnitOfMeasure='{self.UnitOfMeasure}', IVA_Percentage={self.IVA_Percentage}, StockQuantity={self.StockQuantity}, UnitValue={self.UnitValue}, DueDate={self.DueDate}, EntryDate={self.EntryDate}, Category_id={self.Category_id})>"