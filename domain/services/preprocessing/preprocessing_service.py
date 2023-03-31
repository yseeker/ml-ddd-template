from .image1_service import Image1Service
from .image2_service import Image2Service

class ImageCombinationService:
    def __init__(self, image1_service: Image1Service, image2_service: Image2Service):
        self.image1_service = image1_service
        self.image2_service = image2_service

    def combine_images(self, part_image, mask_image):
        # マスク画像を生成する処理
        # ...
        colored_image = self.image2_service.color_fill(part_image)

        edge_detected_image = self.image1_service.detect_edges(part_image)
        # ...

        return combined_image