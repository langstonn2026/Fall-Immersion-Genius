<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clothing App Store</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        .card-image {
            height: 300px;
            overflow: hidden;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Langston's Store</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Gallery</a>
                    </li>
                    <!-- Blank nav link for the genius to complete -->
                    <li class="nav-item">
                      <!-- Genius work starts here -->
                        <a class="nav-link" href="#"> Contact </a>
                      <!-- Genius work ends here -->
                    </li>
                </ul>
            </div>
        </div>
    </nav>
 <!-- Hero Section -->
    <div class="jumbotron text-center py-5" style="background-color: $primary-color; color: $text-color;">
        <h1>Welcome to the Langston's Store</h1>
        <p>Take a deep dive into this ominious store</p>
    <!-- Blank button for the genius to complete -->
        <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#infoModal">
        Learn More Here
        </button>
    </div>
  <!-- Gallery Section -->
    <div class="container my-5">
        <div class="row">
        <!-- Blank card for the genius to complete -->
            <div class="col-md-4">
                <div class="card">
                    <img src="https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/460331/item/goods_09_460331_3x4.jpg?width=369" class="card-img-top card-image" alt="...">
                    <div class="card-body">
                    <!-- Genius work starts here -->
                        <h5 class="card-title">Windproof Outer Fleece Jacket </h5>
                        <p class="card-text"> This fleece jacket features a thin 0.008mm windproof layer for warmth and protection, while maintaining a soft, lightweight feel. It has a smooth microfleece lining, woven accents for style, and a convenient zip chest pocket. Glove-friendly fasteners and microfleece-lined pockets add functionality, with piping at the hem and cuffs for extra insulation. </p>
                        <a href="https://www.uniqlo.com/ca/en/products/E460331-000?colorCode=COL09&sizeCode=SMA003" class="btn btn-primary" target="_blank">View Details</a>
                  <!-- Genius work ends here -->
                    </div>
                </div>
            </div>
        <!-- Additional cards for completed project -->
            <div class="col-md-4">
                <div class="card">
                    <img src="https://images.stockx.com/images/Uniqlo-GU-x-Undercover-Corduroy-Wide-Pants-Black.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1634601068" class="card-img-top card-image" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Corduroy Easy Pants</h5>
                        <p class="card-text">Ideal for both lounging and casual outings, these pants combine comfort and style. They offer a regular fit with a flattering tapered silhouette, providing a modern and relaxed look. Equipped with convenient pockets, they add practicality to their versatile design, making them a great choice for everyday wear.</p>
                        <a href="https://www.uniqlo.com/us/en/products/E471279-000/00?colorDisplayCode=09&sizeDisplayCode=004" class="btn btn-primary" target="_blank">View Details</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <img src="https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/471144/item/goods_09_471144_3x4.jpg?width=400" class="card-img-top card-image" alt="...">
                <div class="card-body">
                    <h5 class="card-title">HEATTECH Souffle Beanie</h5>
                    <p class="card-text">This beanie is designed for both comfort and style, with a relaxed fit that measures 18.9 inches around the head, ensuring it sits comfortably without feeling too tight. Its 8.5-inch height provides ample coverage to keep you warm on chilly days, while maintaining a sleek and modern look. Perfect for everyday wear, it combines practicality with a snug, cozy fit that’s ideal for outdoor activities or simply adding a touch of style to your outfit.</p>
                    <a href="https://www.uniqlo.com/us/en/products/E471144-000/00?colorDisplayCode=09" class="btn btn-primary" target="_blank">View Details</a>
                </div>
            </div>
        </div>
    </div>
<!-- Modal -->
    <div class="modal fade" id="infoModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">About Langston Domain</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                <!-- Genius work starts here -->
                    <p> This gallery holds all the wonders of Langston's supposed "Domain". Take a deep dive into this domain, and you may not want to come back.
                </div>
                <div class="modal-footer">
                <!-- Genius work starts here -->
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"> Close </button>
                <!-- Genius work ends here -->
                </div>
            </div>
        </div>
    </div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
