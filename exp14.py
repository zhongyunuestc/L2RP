__author__ = 's3525116'
__author__ = 's3525116'

from string_manipulation import *
#from reviews import *
#-----------------------------------------------------------------------------------------------------------------------
def parseFileTestData(filename,startFrom):
    '''
      Parsing Stanford Dataset aggressive_dedup.json
      "reviewerID": "A2SUAM1J3GNN3B",
      "asin": "0000013714",
      "reviewerName": "J. McDonald",
      "helpful": [2, 3],
      "reviewText": "I bought this for my husband who plays the piano.  He is having a wonderful time playing these old hymns.  The music  is at times hard to read because we think the book was published for singing from more than playing from.  Great purchase though!",
      "overall": 5.0,
      "summary": "Heavenly Highway Hymns",
      "unixReviewTime": 1252800000,
      "reviewTime": "09 13, 2009"
    :param filename:
    :param entry:
    :return:
    '''
    '''
    :param filename:
    :param entry:
    :return:
    '''
    print("Procedure to Parse Product Review Data of Stanford Dataset aggressive_dedup.json")
    print("Started")
    uniqueReviews = dict()
    #fp = open(filename, 'r')
    counter = 0
    allReviews = []
    listReviews = []
    shouldIStart = 0
    line = ""
    finishAt = startFrom + 100000
    nlinesReadIgnored = 0
    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/allproducts_big_run.txt",'a')
    with open(filename, 'r') as fp:
      for line in fp:

        if counter == finishAt:
            break
        if counter == startFrom:
            print("Starting at index "+str(counter))
            print("Num lines Ignored "+str(nlinesReadIgnored))
            shouldIStart = 1
        else:
            #fp.readline() #toIgnore
            nlinesReadIgnored = nlinesReadIgnored + 1
          #  print("NotConsidered")
          #  print(counter)
          #  print(line)
        if shouldIStart == 1:
            #line = fp.readline()
            #print("Considered")
            #print(counter)
            #print(line)
            new = line.split('reviewerID')
            reviewerID = extractFirstString(new[1])
            #if reviewerID == "":
             #   print("Problem with reviewerID")

            new = line.split('asin')
            asin = extractFirstString(new[1])
            #if asin == "":
             #   print("Problem with asin")

            new = line.split('reviewerName')
            if len(new)>1:
                reviewerName = extractFirstString(new[1])

            #if reviewerName == "":
             #   print("Problem with reviewerName")

            new = line.split('helpful')
            helpful = extractHelpful(new[1])
            if helpful == "":
             #   print("Problem with helpful")
                 for i in range(len(new)):
                    helpful = extractHelpful(new[i])
                    if helpful != "":
                        break

            numVotes = extractNumVotes(new[1])
            #if numVotes == "":
             #   print("Problem with numVotes")

            new = line.split('reviewText')
            reviewText = extractFirstString(new[1])
            #if reviewText == "":
             #   print("Problem with reviewText")


            new = line.split('overall')
            overall = extractRatingTime(new[1])
            if overall == "":
                for i in range(len(new)):
                    overall = extractRatingTime(new[i])
                    if overall != "":
                        break

            #if overall == "":
            #print("Problem with overall")

            new = line.split('summary')
            summary = extractFirstString(new[len(new)-1])
            #if summary == "":
             #   print("Problem with summary")

            new = line.split('unixReviewTime')
            if len(new) > 1:
                unixReviewTime = extractUnixTime(new[1])
            #if unixReviewTime == "":
             #   print("Problem with unixReviewTime")

            new = line.split('reviewTime')
            reviewTime = extractFirstString(new[1])
            #if reviewTime == "":
             #   print("Problem with reviewTime")

            review = Review(reviewerID,asin,reviewTime,helpful,numVotes,overall,reviewText,summary,unixReviewTime)
            filehandle.write(line)
            #filehandle.write("\n")
            if review.productid in uniqueReviews:
               listReviews = uniqueReviews[review.productid]
               listReviews.append(review)
               uniqueReviews[review.productid] = listReviews
            else:
               listReviews = []
               listReviews.append(review)
               uniqueReviews[review.productid] = listReviews
            counter = counter + 1
        else:
            counter = counter + 1
            continue


    filehandle.close()
    fp.close()
    print("Num Reviews")
    print(counter)
    print("Processed "+str(counter)+" Reviews so far")
    print("Finished")
    return uniqueReviews
#-----------------------------------------------------------------------------------------------------------------------
from datetime import datetime
def readDataStanfordDataSetTechniqueTwo(filename,startFrom):
    '''
      Parsing Stanford Dataset aggressive_dedup.json and write each product file with name product id
      "reviewerID": "A2SUAM1J3GNN3B",
      "asin": "0000013714",
      "reviewerName": "J. McDonald",
      "helpful": [2, 3],
      "reviewText": "I bought this for my husband who plays the piano.  He is having a wonderful time playing these old hymns.  The music  is at times hard to read because we think the book was published for singing from more than playing from.  Great purchase though!",
      "overall": 5.0,
      "summary": "Heavenly Highway Hymns",
      "unixReviewTime": 1252800000,
      "reviewTime": "09 13, 2009"
    :param filename:
    :param entry:
    :return:
    '''
    '''
    :param filename:
    :param entry:
    :return:
    '''
    print("Procedure to Parse Product Review Data of Stanford Dataset aggressive_dedup.json")
    print("Started at ")
    start = datetime.now()
    print(start)
    uniqueReviews = dict()
    #numReviesPerProduct = dict()
    fp = open(filename, 'r')
    counter = 0
    allReviews = []
    listReviews = []
    shouldIStart = 0
    line = ""
    finishAt = startFrom + 2000000
    while 1:
        if counter == finishAt:
            break
        if counter == startFrom:
            print("Starting at index "+str(counter))
            shouldIStart = 1
        else:
             line = fp.readline() #toIgnore
        if shouldIStart == 1:
            line = fp.readline()

            new = line.split('reviewerID')
            reviewerID = extractFirstString(new[1])
            #if reviewerID == "":
             #   print("Problem with reviewerID")

            new = line.split('asin')
            asin = extractFirstString(new[1])
            #if asin == "":
             #   print("Problem with asin")

            new = line.split('reviewerName')
            if len(new)>1:
                reviewerName = extractFirstString(new[1])

            #if reviewerName == "":
             #   print("Problem with reviewerName")

            new = line.split('helpful')
            helpful = extractHelpful(new[1])
            if helpful == "":
             #   print("Problem with helpful")
                 for i in range(len(new)):
                    helpful = extractHelpful(new[i])
                    if helpful != "":
                        break

            numVotes = extractNumVotes(new[1])
            #if numVotes == "":
             #   print("Problem with numVotes")

            new = line.split('reviewText')
            reviewText = extractFirstString(new[1])
            #if reviewText == "":
             #   print("Problem with reviewText")


            new = line.split('overall')
            overall = extractRatingTime(new[1])
            if overall == "":
                for i in range(len(new)):
                    overall = extractRatingTime(new[i])
                    if overall != "":
                        break

            #if overall == "":
            #print("Problem with overall")

            new = line.split('summary')
            summary = extractFirstString(new[len(new)-1])
            #if summary == "":
             #   print("Problem with summary")

            new = line.split('unixReviewTime')
            if len(new) > 1:
                unixReviewTime = extractUnixTime(new[1])
            #if unixReviewTime == "":
             #   print("Problem with unixReviewTime")

            new = line.split('reviewTime')
            reviewTime = extractFirstString(new[1])
            #if reviewTime == "":
             #   print("Problem with reviewTime")

            review = Review(reviewerID,asin,reviewTime,helpful,numVotes,overall,reviewText,summary,unixReviewTime)
            filehandle = None
            try:
                filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_two/"+review.productid,'a')
                writeReviewToFile(filehandle,review)
            except OSError as e:
                to = e.errno
            finally:
                if filehandle is not None:
                    filehandle.close()
                '''
            print(counter)
            if review.productid in uniqueReviews:
               filehandle = uniqueReviews[review.productid]
               writeReviewToFile(filehandle,review)
               #filehandle.close()
            else:
                try:
                    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_two/"+review.productid,'a')
                    writeReviewToFile(filehandle,review)
                    uniqueReviews[review.productid] = filehandle
                except OSError as e:
                    to = e.errno
            print(counter)

            if review.productid in uniqueReviews:
               filehandle = uniqueReviews[review.productid]
               writeReviewToFile(filehandle,review)
               filehandle.close()
               #numReviesPerProduct[review.productid] = numReviesPerProduct[review.productid] +1
            else:
                print(counter)
                writeReviewToFile(filehandle,review)
                uniqueReviews[review.productid] = filehandle
                filehandle.close()
               #numReviesPerProduct[review.productid] = 1
            '''
            counter = counter + 1


    print("Processed "+str(counter)+" Reviews so far")
    print("Num Reviews processed in this run")
    print(counter-startFrom)
    print("Num Unique Products")
    #print(len(uniqueReviews))
    '''
    countNumProducts = 0
    print("Num Products with 20 reviews or more ")
    for key,value in numReviesPerProduct.items():
        if value >19:
            countNumProducts = countNumProducts + 1
    print(countNumProducts)
    '''
    Finished = datetime.now()
    print("Finished at ")
    print(Finished)
    print("Taking ")
    done = Finished - start
    print(str(round(done.total_seconds()/60,3))+" minutes")
    return #numReviesPerProduct
#-----------------------------------------------------------------------------------------------------------------------
def readDataStanfordDataSetTechniqueOne():
    print("Started at ")
    start = datetime.now()
    print(start)
    uniqueReviews= parseFileTestData("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/aggressive_dedup.json/aggressive_dedup.json.gz2",0)
    print("Num Unique Products")
    print(len(uniqueReviews))
    countNumProducts = 0
    totalNumReviews = 0
    for key,value in uniqueReviews.items():
           numReviews = len(value)
           if numReviews > 19:
            valid = writeEachProductReviewsToFile(key,value,"C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_one-p2/")
            if valid == 1:
                countNumProducts = countNumProducts + 1
                totalNumReviews = totalNumReviews + numReviews
    print("Num Products with 20 reviews or more ")
    print(countNumProducts)
    print("With Total Num Reviews")
    print(totalNumReviews)
    Finished = datetime.now()
    print("Finished at ")
    print(Finished)
    print("Taking ")
    done = Finished - start
    print(str(round(done.total_seconds()/60,3))+" minutes")
    return
#-----------------------------------------------------------------------------------------------------------------------
def readDataStanfordDataSetTechniqueThree(filename):
    print("Procedure to Parse Product Review Data of Stanford Dataset aggressive_dedup.json")
    print("Started")
    uniqueReviews = dict()
    #fp = open(filename, 'r')
    counter = 0
    allReviews = []
    listReviews = []
    shouldIStart = 0
    start = datetime.now()
    print("Started Searching for Products with reviews >= 20 at")
    print(start)
    line = ""
    startFrom = 0
    #finishAt = 10000
    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/products_with_big_reviews.txt",'a')
    with open(filename, 'r') as fp:
      for line in fp:
        #if counter == finishAt:
         #   break
        if counter == startFrom:
            shouldIStart = 1

        if shouldIStart == 1:

            new = line.split('asin')
            asin = extractFirstString(new[1])

            if asin in uniqueReviews:
               numReviews = uniqueReviews[asin]
               numReviews = numReviews + 1
               uniqueReviews[asin] = numReviews
            else:
               uniqueReviews[asin] = 0

            counter = counter + 1
        else:
            counter = counter + 1
            continue
    Finished = datetime.now()
    done = Finished - start
    print("Finished Searching in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Now Writing values to file")
    for key,value in uniqueReviews.items():
           if value > 19:
             filehandle.write(key)
             filehandle.write("\t")
             filehandle.write(str(value))
             filehandle.write("\n")

    FinishedWriting = datetime.now()
    done = FinishedWriting - done
    #print("Finished Writing in "+str(round(done.total_seconds()/60,3))+" minutes")
    filehandle.close()
    fp.close()

    print("Num Reviews")
    print(counter)
    print("Processed "+str(counter)+" Reviews so far")
    FinishedAll = datetime.now()
    done = FinishedAll - start
    print("Finished the process in "+str(round(done.total_seconds()/60,3))+" minutes")

    return
#-----------------------------------------------------------------------------------------------------------------------
def parseReviewLineStanfordDataset(line):

    new = line.split('reviewerID')
    reviewerID = extractFirstString(new[1])

    new = line.split('asin')
    asin = extractFirstString(new[1])

    reviewerName = ""
    new = line.split('reviewerName')
    if len(new)>1 :
        reviewerName = extractFirstString(new[1])

    new = line.split('helpful')
    helpful = extractHelpful(new[1])
    if helpful == "":
         for i in range(len(new)):
            helpful = extractHelpful(new[i])
            if helpful != "":
                break

    numVotes = extractNumVotes(new[1])

    new = line.split('reviewText')
    reviewText = extractFirstString(new[1])

    new = line.split('overall')
    overall = extractRatingTime(new[1])
    if overall == "":
        for i in range(len(new)):
            overall = extractRatingTime(new[i])
            if overall != "":
                break

    new = line.split('summary')
    summary = extractFirstString(new[len(new)-1])

    unixReviewTime = 0
    new = line.split('unixReviewTime')
    if len(new) > 1:
        unixReviewTime = extractUnixTime(new[1])

    new = line.split('reviewTime')
    reviewTime = extractFirstString(new[1])

    review = Review(reviewerID,asin,reviewTime,helpful,numVotes,overall,reviewText,summary,unixReviewTime)

    return review
def parseReviewLineStanfordDatasetMinimized(line):
    new = line.split('\t')
    reviewerID = new[0]
    asin = new[1]
    reviewerName = ""
    reviewTime = new[2]
    numVotes = new[3]
    helpful = new[4]
    overall = new[5]
    reviewText = new[6]
    summary = new[7]
    unixReviewTime = new[8]
    review = Review(reviewerID,asin,reviewTime,helpful,numVotes,overall,reviewText,summary,unixReviewTime)
    return review
def writeListofReviews(listOfReviews):
    for review in listOfReviews:
        filehandle = None
        try:
            filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+review.productid+".txt",'a')
            writeReviewToFile(filehandle,review)
        except OSError as e:
            to = e.errno
    return
def writeListofReviewsNew(listOfReviews,AllFiles):

    numFilesWritten = 0
    for key,value in listOfReviews.items():
        filehandle = None
        if value != "":
            try:
                filehandle = AllFiles[key]
                try:
                    filehandle.write(value)
                    numFilesWritten = numFilesWritten +1
                except IOError as e:
                    pass
            except KeyError as e:
                    if len(AllFiles) >= 500:
                         #filehandle = AllFiles[0]
                         #del AllFiles[0]
                         #filehandle.close()
                         AllFiles.clear()
                         try:
                             filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+key+".txt",'a')
                             filehandle.write(value)
                             AllFiles[key] = filehandle
                             numFilesWritten = numFilesWritten +1
                         except IOError as e:
                             pass
                    else:
                        try:
                            filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+key+".txt",'a')
                            filehandle.write(value)
                            AllFiles[key] = filehandle
                            numFilesWritten = numFilesWritten +1
                        except IOError as e:
                            pass

    print("Num Files written in this round " +str(numFilesWritten))
    return
def writeListofReviewsNewNew(listOfReviews):
    numFilesWritten = 0
    counter = 0
    numLen = len(listOfReviews)
    for key,value in listOfReviews.items():
      filehandle = None
      if value != "":
             try:
                 fileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+key+".txt"
                 try:
                     filehandle = open(fileName,'a')#open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+key+".txt",'a')
                     filehandle.write(value)
                     numFilesWritten = numFilesWritten +1
                 except IOError as e:
                     pass
             except KeyError as e:
                 pass
      counter = counter + 1
      if counter%10000 == 0:
          print(str(counter) +" is done out of "+str(numLen))


    print("Num Files written in this round " +str(numFilesWritten))
    return
def writeOneFileToImportantProducts(listOfReviews,filehandle):

    numFilesWritten = 0
    for key,value in listOfReviews.items():
      #filehandle = None
      if value != "":
        try:
             filehandle.write(value)
             numFilesWritten = numFilesWritten +1
        except IOError as e:
             pass

    print("Num Files written in this round " +str(numFilesWritten))
    return
def convertReviewtoText(review):
    '''
    reviewString = review.memberid
    reviewString = reviewString + "\t"+review.productid
    reviewString = reviewString + "\t"+review.date
    reviewString = reviewString + "\t"+str(review.numfeedback)
    reviewString = reviewString + "\t"+str(review.numhelpful)
    reviewString = reviewString + "\t"+str(review.rating)
    reviewString = reviewString + "\t"+review.body
    reviewString = reviewString + "\t"+review.summary
    reviewString = reviewString + "\t"+str(review.unixtime) + "\n"
    '''

    reviewString = ''.join([review.memberid, "\t",review.productid,"\t",review.date,"\t",str(review.numfeedback),"\t",str(review.numhelpful),"\t",str(review.rating),"\t",review.body,"\t",review.summary,"\t",str(review.unixtime),"\n"])
    #print("reviewString")
    #print(reviewString)
    return reviewString
#-----------------------------------------------------------------------------------------------------------------------
#import sys
def retrieveProductReviewsPerProduct(filename):
    print("Procedure to retrieve all reviews for product from Stanford Dataset aggressive_dedup.json")
    print("Started")
    counter = 0
    shouldIStart = 0
    start = datetime.now()
    print(start)
    line = ""
    print("Reading all available products with the criteria")
    productList = retrieveAllProductsFromProductReviewFile("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/products_with_big_reviews.txt")
    #allFileHandles = createfileHandlesForAllProducts(productList)
    step1Finished = datetime.now()
    done = step1Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")

    '''
    print("Creating dicrionary with opened files to write reviews")

    productFileHandle = dict([(product, open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+product+".txt",'a')) for product in productList])

    step2Finished = datetime.now()
    done = step2Finished - step1Finished
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    '''
    AllFiles = dict()

    counter = 0
    numRightReviews = 0
    print("Retrieving all reviews for all product files")
    listofReviews = dict()
    listRev = []
    currentIndex = 0
    previous = step1Finished
    with open(filename, 'r') as fp:
      for line in fp:
        new = line.split('\t')
        if len(new) > 1:
            asin = new[1]
            if asin != "":
                try:
                    productId = productList[asin]
                    if asin == productId:
                        numRightReviews = numRightReviews + 1
                        '''
                        try:
                            fileName = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+asin+".txt"
                            filehandle = open(fileName,'a')
                            filehandle.write(line)
                        except IOError as e:
                            pass
                        '''
                        if currentIndex == 10000000:
                            beforeWriting = datetime.now()
                            print("Will start writing")
                            writeListofReviewsNewNew(listofReviews)
                            afterWriting = datetime.now()
                            done = afterWriting - beforeWriting
                            print(" Writing took "+str(round(done.total_seconds()/60,3)))
                            listofReviews = dict()
                            currentIndex = 0
                            listofReviews[asin] = line
                        else:
                            try:
                                availableString = listofReviews[asin]
                                availableString = ''.join([availableString, line])
                                listofReviews[asin] = availableString
                            except KeyError as e:
                                listofReviews[asin] = line
                        currentIndex = currentIndex + 1

                except KeyError as e:
                    pass
            counter = counter + 1

            if counter%100000 == 0:
                now = datetime.now()
                done = now - previous
                previous = now
                done2 = now - step1Finished
                print(str(counter)+" all Processed "+str(numRightReviews)+" good this step took "+str(round(done.total_seconds()/60,3))+" minutes" + " out of "+str(round(done2.total_seconds()/60,3))+" minutes")
    if len(listofReviews) > 0 :
        print("Writing what's leftover")
        writeListofReviewsNewNew(listofReviews)
    step3Finished = datetime.now()
    done = step3Finished - step1Finished
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")

    Finished = datetime.now()
    done = Finished - start
    print("Finished retrieving all reviwes for this product in "+str(round(done.total_seconds()/60,3))+" minutes")
    fp.close()
    return
#-----------------------------------------------------------------------------------------------------------------------
def retrieveAllProductsFromProductReviewFile(filename):

    data_initial = open(filename, "rU")
    productList = []
    reader = csv.reader((line.replace('\0','') for line in data_initial), delimiter='\n')
    for row in reader:
        temp = [i.split('\t') for i in row]
        temp = list(temp[0])
        productList.append(temp[0])

    productsFound = dict([(product, product) for product in productList])
    return productsFound
def createfileHandlesForAllProducts(productList):
    print("Creating All empty files first")
    allFileHandles = dict()
    start = datetime.now()
    counter = 0
    print(start)
    for key,value in productList.items():
      fileName = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+key+".txt"
      try:
          filehandle = open(fileName,'a')
          filehandle.close()
          allFileHandles[key] = fileName
      except IOError as e:
          pass
      counter = counter + 1
      if counter%100000 == 0:
          print(str(counter)+" done so far")
    finished = datetime.now()
    done = finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return allFileHandles
def createSmallerDatasSetFile(filename):

    print("Procedure to create Smaller DataSet from Stanford Dataset aggressive_dedup.json")
    print("Started")
    counter = 0
    shouldIStart = 0
    start = datetime.now()
    print(start)
    line = ""
    print("Reading all available products with the criteria")
    productList = retrieveAllProductsFromProductReviewFile("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/products_with_big_reviews.txt")
    step1Finished = datetime.now()
    done = step1Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/aggressive_dedup_smaller.txt",'a')
    filehandle.write(line)
    counter = 0
    numRightReviews = 0
    previous = step1Finished
    print("Retrieving all reviews for all product files")
    with open(filename, 'r') as fp:
      for line in fp:
        new = line.split('asin')
        if len(new) > 1:
            asin = extractFirstString(new[1])
            if asin != "":
                try:
                    var1 = productList[asin]
                    if asin == var1:
                        numRightReviews = numRightReviews + 1
                        review = parseReviewLineStanfordDataset(line)
                        reviewString = convertReviewtoText(review)
                        filehandle.write(reviewString)
                        filehandle.write("\n")
                except KeyError as e:
                    pass
            counter = counter + 1

            if counter%100000 == 0:
                now = datetime.now()
                done = now - previous
                previous = now
                done2 = now - step1Finished
                print(str(counter)+" all Processed "+str(numRightReviews)+" good this step took "+str(round(done.total_seconds()/60,3))+" minutes" + " out of "+str(round(done2.total_seconds()/60,3))+" minutes")

    step3Finished = datetime.now()
    done = step3Finished - step1Finished
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    print("Finished retrieving all reviwes for this product in "+str(round(done.total_seconds()/60,3))+" minutes")
    fp.close()
    return
#-----------------------------------------------------------------------------------------------------------------------
def readMetaDataFileAndWriteOnlyNeeded(filePath):
    print("Procedure to retrieve all metaData for product from Stanford Dataset metadata.json")
    print("Started")
    counter = 0
    shouldIStart = 0
    start = datetime.now()
    print(start)
    line = ""
    print("Reading all available products with the criteria")
    productList = retrieveAllProductsFromProductReviewFile("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/products_with_big_reviews.txt")

    step1Finished = datetime.now()
    done = step1Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")

    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/metadata.json/MetaDataSet.txt",'a')
    counter = 0
    numRightReviews = 0
    print("Retrieving all MetaData for all product files")
    listofReviews = ""
    currentIndex = 0
    previous = step1Finished
    with open(filePath, 'r') as fp:

      for line in fp:
        new = line.split('asin')
        asin = extractAsin(new[1])
        if asin != "":
            try:
                var1 = productList[asin]
                if asin == var1:
                    filehandle.write(line)
                    numRightReviews = numRightReviews + 1
            except KeyError as e:
                pass

        counter = counter + 1

        if counter%100000 == 0:
            now = datetime.now()
            done = now - previous
            previous = now
            done2 = now - step1Finished
            print(str(counter)+" all Processed "+str(numRightReviews)+" good this step took "+str(round(done.total_seconds()/60,3))+" minutes" + " out of "+str(round(done2.total_seconds()/60,3))+" minutes")

    step3Finished = datetime.now()
    done = step3Finished - step1Finished
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    print("Finished retrieving all reviwes for this product in "+str(round(done.total_seconds()/60,3))+" minutes")
    fp.close()
    return
def createNewMetaDataWithOnlySalesRank(filePath):
    print("Procedure to write MetaData File with only Product Id and Sales Rank")
    print("Started")
    counter = 0
    start = datetime.now()
    previous = start
    print(start)
    line = ""
    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/metadata.json/Metadata_Sales_Rank.txt",'a')
    counter = 0
    with open(filePath, 'r') as fp:
      for line in fp:

        new = line.split('asin')
        asin = extractAsin(new[1])
        new = line.split('salesRank')
        if len(new)>1:
            salesRank = extractSalesRank(new[1])
        else:
            salesRank = ("None", -1)

        filehandle.write(str(asin))
        filehandle.write("\t")
        filehandle.write(salesRank[0])
        filehandle.write("\t")
        filehandle.write(str(salesRank[1]))
        filehandle.write("\n")

        if counter%100000 == 0:
            now = datetime.now()
            done = now - previous
            previous = now
            print(str(counter)+" all Processed "+str(round(done.total_seconds()/60,3))+" minutes")

        counter = counter + 1
    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    print("Finished retrieving all reviwes for this product in "+str(round(done.total_seconds()/60,3))+" minutes")
    fp.close()
    return
def readSalesRankMetaDataFile(filePath):
    print("Procedure to read MetaData File with only Product Id and Sales Rank")
    print("Started")
    counter = 0
    start = datetime.now()
    previous = start
    print(start)
    line = ""
    categories = dict()
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           try:
                numProducts = categories[row[1]]
                categories[row[1]] = numProducts + 1
           except KeyError as e:
                categories[row[1]] = 1
                pass
    counter = 0
    for key,value in categories.items():
        print(key+" = "+str(value))
        counter = counter + value
    print("Total Number of all Products = "+str(counter))
    return
#-----------------------------------------------------------------------------------------------------------------------

def readSalesRankMetaAndCreateFilesWithCategories(filePath):
    print("Procedure to read MetaData File and create files for each category")
    print("This file willl contain each product_ID Sales_Rank")
    #product_Id Category sales_rank
    print("Started")
    start = datetime.now()
    previous = start
    print(start)
    counter = 0
    line = ""
    products = []
    categories = dict()
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           try:
                products = categories[row[1]]
                products.append((row[0],int(row[2])))
                categories[row[1]] = products
           except KeyError as e:
                products = []
                products.append((row[0],int(row[2])))
                categories[row[1]] = products
                pass

    for key,value in categories.items():
        print("key")
        print(key)
        if key !="":
            filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories/"+key+".txt",'a')
            for i in range(len(value)):
                filehandle.write(str(value[i][0]))
                filehandle.write("\t")
                filehandle.write(str(value[i][1]))
                filehandle.write("\n")

    Finished = datetime.now()
    done = Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")

    return

def computeMajorityVoteForProductCategories(filePath,category):
    print("Procedure to read category File, get a product from it and read its file and compute the average and write to a file for a cetegory file")
    print("This file willl contain each product_ID Sales_Rank")
    print("Considering "+category)
    #product_Id Category sales_rank
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    filehandle = open("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories_rating/"+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           fileName = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0
           try:
              with open(fileName, 'r') as filep:
                for item in filep:
                    review = item.split('\t')
                    overallRate = overallRate + float(review[5])
                    counter = counter + 1
           except IOError as e:
              pass
           filehandle.write(productId)
           filehandle.write("\t")
           overallRate = overallRate/counter
           overallRate = round(overallRate,4)
           filehandle.write(str(overallRate))
           filehandle.write("\n")

    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
def computeMajorityVoteForProductCategoriesWithUserExpert(filePath,category,destDirectory):
    print("Procedure to read category File, get a product from it and read its file and compute the average and write to a file for a cetegory file")
    print("This file willl contain each product_ID Sales_Rank")
    print("Considering "+category)
    #product_Id Category sales_rank
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    #Load User Expertiese per category
    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\UserHelpfulVotesPerCategory/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = int(row[1])

    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           fileName = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0
           try:
              with open(fileName, 'r') as filep:
                for item in filep:
                    review = item.split('\t')
                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0
                    numHelpful = int(review[4])
                    weight = 0
                    if maxVotes > 0:
                        weight = float(numHelpful/maxVotes)
                        overallRate = overallRate + weight*float(review[5])
                        counter = counter + 1
           except IOError as e:
              pass
           filehandle.write(productId)
           filehandle.write("\t")
           if counter > 0:
            overallRate = overallRate/counter
           overallRate = round(overallRate,4)
           filehandle.write(str(overallRate))
           filehandle.write("\n")

    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
def computeMajorityVoteForProductCategoriesDateFreshnessAdjusted(filePath,category,destDirectory):
    print("Procedure to compute product rate per category based on date freshness adjusted")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0

           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           productRates = []
           reviewweights = []
           numoccurnecess = dict()
           weights = []
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')
                    productRates.append(float(review[5]))
                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    if len(datesplit)>1 and datesplit[1]!=' ' and len(datesplit[1])<=5:
                        year = int(datesplit[1])
                        month = int(month)
                        day = int(day)
                        currentDay = datetime(year, month, day)

                        productDates.append((currentDay))
                        if currentDay >maxDate:
                            maxDate = currentDay
                        if currentDay <minDate:
                            minDate = currentDay

              overallRate = 0
              for i in range(len(productDates)):

                  up = (productDates[i]-minDate).days
                  up = float(up)
                  down = (maxDate-minDate).days
                  down = float(down)

                  dateFactor = float(up/down)
                  bfound = 0
                  for item in weights:
                        if dateFactor == item:
                            bfound = 1
                            break
                  if bfound == 0:
                        weights.append(dateFactor)
                  try:
                        num = numoccurnecess[dateFactor]
                        numoccurnecess[dateFactor] = num + 1

                  except KeyError as e:
                        numoccurnecess[dateFactor] = 1
                  reviewweights.append(dateFactor)
                  #overallRate = overallRate + productRates[i]*dateFactor
              sumweights = 0
              for item in weights:
                    sumweights = sumweights + item
              weightDict = dict()
              for item in weights:
                    weightDict[item] = item/sumweights

              index = 0
              for wi in reviewweights:
                    newweight = weightDict[wi]
                    numo = numoccurnecess[wi]
                    newweight = newweight/numo
                    overallRate = overallRate + newweight*productRates[index]
                    index = index + 1
              #overallRate = overallRate/len(productDates)
              overallRate = round(overallRate,4)

              filehandle.write(productId)
              filehandle.write("\t")
              overallRate = round(overallRate,4)
              filehandle.write(str(overallRate))

              filehandle.write("\n")

           except IOError as e:
              pass

    filehandle.close()

    Finished = datetime.now()
    print("Finished")
    print(Finished)
    done = Finished - start
    print("done")

    return
def computeMajorityVoteForProductCategoriesDateFreshness(filePath,category,destDirectory):

    print("Procedure to compute product rate per category based on date freshness")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0

           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           productRates = []
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')
                    productRates.append(float(review[5]))
                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    if len(datesplit)>1 and datesplit[1]!=' ' and len(datesplit[1])<=5:
                        year = int(datesplit[1])
                        month = int(month)
                        day = int(day)
                        currentDay = datetime(year, month, day)

                        productDates.append((currentDay))
                        if currentDay >maxDate:
                            maxDate = currentDay
                        if currentDay <minDate:
                            minDate = currentDay

              overallRate = 0
              for i in range(len(productDates)):

                  up = (productDates[i]-minDate).days
                  up = float(up)
                  down = (maxDate-minDate).days
                  down = float(down)

                  dateFactor = float(up/down)
                  overallRate = overallRate + productRates[i]*dateFactor

              overallRate = overallRate/len(productDates)
              overallRate = round(overallRate,4)

              filehandle.write(productId)
              filehandle.write("\t")
              overallRate = round(overallRate,4)
              filehandle.write(str(overallRate))

              filehandle.write("\n")

           except IOError as e:
              pass

    filehandle.close()

    Finished = datetime.now()
    print("Finished")
    print(Finished)
    done = Finished - start
    print("done")
	#print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
def computeMajorityVoteForProductCategoriesWithUserExpertTest(filePath,category,destDirectory):
    print("Procedure to test Num Votes Calculation in new Way")
    print("Considering "+category)
    #product_Id Category sales_rank
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    #Load User Expertiese per category
    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategory/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = int(row[1])
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           fileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0
           weights=[]
           reviewweights = []
           rates = []
           numoccurnecess = dict()
           try:
              with open(fileName, 'r') as filep:
                for item in filep:
                    review = item.split('\t')
                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0
                    numHelpful = int(review[4])

                    if maxVotes == 0:
                        maxVotes = 10
                    else:
                        maxVotes = maxVotes*1.5

                    if numHelpful == 0:
                        numHelpful = 5
                    else:
                        numHelpful = numHelpful*1.5

                    weight = 0
                    if maxVotes < numHelpful:
                        temp = maxVotes
                        maxVotes = numHelpful
                        numHelpful = temp

                    weight = float(float(numHelpful)/float(maxVotes))

                    bfound = 0
                    for item in weights:
                        if weight == item:
                            bfound = 1
                            break
                    if bfound == 0:
                        weights.append(weight)
                    try:
                        num = numoccurnecess[weight]
                        numoccurnecess[weight] = num + 1

                    except KeyError as e:
                        numoccurnecess[weight] = 1

                    reviewweights.append(weight)
                    rates.append(float(review[5]))
                sumweights = 0
                for item in weights:
                    sumweights = sumweights + item
                weightDict = dict()
                for item in weights:
                    weightDict[item] = item/sumweights

                index = 0
                for wi in reviewweights:
                    newweight = weightDict[wi]
                    numo = numoccurnecess[wi]
                    newweight = newweight/numo
                    overallRate = overallRate + newweight*rates[index]
                    index = index + 1



           except IOError as e:
              pass
           filehandle.write(productId)
           filehandle.write("\t")

           overallRate = round(overallRate,4)
           filehandle.write(str(overallRate))
           filehandle.write("\n")

    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("finished")
    print(Finished)
    return
def computeMajorityVoteForProductCategoriesWithUserExpertAdjusted(filePath,category,destDirectory):

    print("Procedure to weighted vote adjusted")
    print("Considering "+category)
    #product_Id Category sales_rank
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    #Load User Expertiese per category
    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategory/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = int(row[1])

    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           fileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0
           try:
              with open(fileName, 'r') as filep:
                for item in filep:
                    review = item.split('\t')
                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0
                    numHelpful = int(review[4])

                    if maxVotes == 0:
                        maxVotes = 10
                    else:
                        maxVotes = maxVotes*1.5
                    if numHelpful == 0:
                        numHelpful = 5
                    else:
                        numHelpful = numHelpful*1.5

                    weight = 0
                    if maxVotes > 0:
                        weight = float(float(numHelpful)/float(maxVotes))
                        overallRate = overallRate + weight*float(review[5])
                        counter = counter + 1
           except IOError as e:
              pass
           filehandle.write(productId)
           filehandle.write("\t")
           if counter > 0:
            overallRate = overallRate/counter
           overallRate = round(overallRate,4)
           filehandle.write(str(overallRate))
           filehandle.write("\n")

    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    print("done")
    return
def computeRateNumVotesDatesAdjusted(filePath,category,destDirectory):

    print("Procedure to compute product rate per category based on 0.3 NumVotes and 0.7 date freshness Adjusted")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategory/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = int(row[1])

    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           weights=[]
           reviewweights = []
           rates = []
           numoccurnecess = dict()
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')
                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0
                    numHelpful = int(review[4])

                    if maxVotes == 0:
                        maxVotes = 10
                    else:
                        maxVotes = maxVotes*1.5

                    if numHelpful == 0:
                        numHelpful = 5
                    else:
                        numHelpful = numHelpful*1.5

                    weight = 0
                    if maxVotes < numHelpful:
                        temp = maxVotes
                        maxVotes = numHelpful
                        numHelpful = temp

                    weight = float(float(numHelpful)/float(maxVotes))

                    bfound = 0
                    for item in weights:
                        if weight == item:
                            bfound = 1
                            break
                    if bfound == 0:
                        weights.append(weight)
                    try:
                        num = numoccurnecess[weight]
                        numoccurnecess[weight] = num + 1

                    except KeyError as e:
                        numoccurnecess[weight] = 1

                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    if len(datesplit)>1 and datesplit[1]!=' ' and len(datesplit[1])<=5:
                        year = int(datesplit[1])
                        month = int(month)
                        day = int(day)
                        currentDay = datetime(year, month, day)

                        productDates.append((currentDay))
                        if currentDay >maxDate:
                            maxDate = currentDay
                        if currentDay <minDate:
                            minDate = currentDay


                    reviewweights.append(weight)
                    rates.append(float(review[5]))
                sumweights = 0
                for item in weights:
                    sumweights = sumweights + item
                weightDict = dict()
                for item in weights:
                    weightDict[item] = item/sumweights

                index = 0
                overallRateVotes = 0
                for wi in reviewweights:
                    newweight = weightDict[wi]
                    numo = numoccurnecess[wi]
                    newweight = newweight/numo
                    overallRateVotes = overallRateVotes + newweight*rates[index]
                    index = index + 1


                numoccurnecess = dict()
                weights = []
                reviewweights = []
                overallRateDate = 0
                for i in range(len(productDates)):

                  up = (productDates[i]-minDate).days
                  up = float(up)
                  down = (maxDate-minDate).days
                  down = float(down)

                  dateFactor = float(up/down)
                  bfound = 0
                  for item in weights:
                        if dateFactor == item:
                            bfound = 1
                            break
                  if bfound == 0:
                        weights.append(dateFactor)
                  try:
                        num = numoccurnecess[dateFactor]
                        numoccurnecess[dateFactor] = num + 1

                  except KeyError as e:
                        numoccurnecess[dateFactor] = 1

                  reviewweights.append(dateFactor)


              sumweights = 0
              for item in weights:
                    sumweights = sumweights + item
              weightDict = dict()


              for item in weights:
                    weightDict[item] = item/sumweights

              index = 0

              for wi in reviewweights:

                    newweight = weightDict[wi]
                    numo = numoccurnecess[wi]
                    newweight = newweight/numo
                    overallRateDate = overallRateDate + newweight*rates[index]
                    index = index + 1


              finalRate = 0.7*overallRateDate + 0.3*overallRateVotes

              filehandle.write(productId)
              filehandle.write("\t")
              finalRate = round(finalRate,4)
              filehandle.write(str(finalRate))
              filehandle.write("\n")
           except IOError as e:
              pass

    filehandle.close()

    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    return

import math
def computeRateNumVotesDatesExponential(filePath,category,destDirectory):
    print("Procedure to compute product rate per category based on date only exponential")
    #category = "Prime Pantry"
    #filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/Prime Pantry.txt"
    #category = "Books"
    #filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/Books.txt"
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""

    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = float(row[3])

    numReviesPerProdcut = []
    products = []
    previousWeights = []
    numGoodReviews = 0
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           weights=[]
           rates = []
           reviewHelpfulWeight = []
           extrweights = []
           numoccurnecess = dict()
           #print("CurrentDate "+" "+ " "+" Time Diff" +" "+ "MaxWeight"+" "+"ExpValue")
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')
                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0

                    numHelpful = int(review[4])
                    numtotalVotes = 0
                    if review[3] !="":
                        numtotalVotes = int(review[3])

                    weightMaxHelpVotes = 0
                    extraWei = 0
                    if maxVotes >0 :
                        weightMaxHelpVotes = float(float(numHelpful)/float(maxVotes))
                    if numtotalVotes > 0:
                        extraWei = float(float(numHelpful)/float(numtotalVotes))

                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    if len(datesplit)>1 and datesplit[1]!=' ' and len(datesplit[1])<=5:
                        year = int(datesplit[1])
                        month = int(month)
                        day = int(day)
                        currentDay = datetime(year, month, day)

                        productDates.append((currentDay))
                        if currentDay >maxDate:
                            maxDate = currentDay
                        if currentDay <minDate:
                            minDate = currentDay

                        #reviewHelpfulWeight.append(weightMaxHelpVotes)
                        reviewHelpfulWeight.append(userExpert[review[0]])
                        rates.append(float(review[5]))
                        if float(review[5]) > 3:
                            numGoodReviews = numGoodReviews + 1

                        extrweights.append(extraWei)

                newweights = []
                index = 0
                #print("-------------------------------------------------")
                dayweights = []
                credweights = []

                for revweighthelp in reviewHelpfulWeight:
                    timeDiff = (productDates[index]-minDate).days
                    beta = 0.01
                    part2 = revweighthelp
                    part1 = beta*timeDiff
                    #print("--------------")
                    part1 = part1/2
                    part2 = part2 + part1/2

                    #dayweights.append(part1)
                    #credweights.append(part2)
                    #print(productDates[index])
                    #print(part1)
                    #print(revweighthelp)
                    #print(part2)
                    part3 = part1#+ part2
                    #print(part3)
                    expValue = (math.e** part3 )
                    #print(expValue)
                    newweights.append(expValue)
                    index = index + 1

                index = 0
                minVal = 100000000
                maxVal = -10000000
                '''
                sumdayweights = 0
                for dayweight in dayweights:
                    sumdayweights = sumdayweights + dayweight
                for dayweight in dayweights:
                    part1 = (dayweight/sumdayweights)*2
                    part2 = credweights[index]*1
                    print(part1)
                    print(part2)
                    part3 = part1 + part2
                    print(part3)
                    expValue = (math.e** part3 )*1000
                    print(expValue)
                    print("--------------------------")
                    newweights.append(expValue)
                    index = index + 1
                '''
                index = 0
                for item in newweights:
                    if item >maxVal:
                        maxVal = item
                    if item <minVal:
                        minVal = item
                newFinalRate = 0

                for item in newweights:
                  newWeight = float((float((item-minVal))/float((maxVal-minVal))))
                  newRate = newWeight*rates[index]
                  #print("new Weight")
                  #print(newRate)
                  newFinalRate = newFinalRate + newRate
                  index = index + 1

                previousWeights.append(newFinalRate)
                products.append(productId)


           except IOError as e:
              pass

    minVal = 10000
    maxVal = -1000

    for item in previousWeights:
        if item >maxVal:
            maxVal = item
        if item <minVal:
            minVal = item
    index = 0
    for product in products:
        #print("product")
        #print(product)
        filehandle.write(product)
        filehandle.write("\t")
        newFinalRate = ((float(previousWeights[index]) -minVal)/(float(maxVal-minVal)))*5
        #newFinalRate = previousWeights[index]
        filehandle.write(str(newFinalRate))
        filehandle.write("\n")
        index = index + 1

    filehandle.close()

    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    return
def computeRankForBaseline(filePath,category,destDirectory):
    print("Procedure to compute Baseline Method")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    products = []
    previousWeights = []
    SentiFile = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/ProductReviewSenti"+category+".txt",'a')
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           weights=[]
           rates = []
           reviewHelpfulWeight = []
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')

                    numHelpful = int(review[4])
                    numtotalVotes = 0
                    if review[3] !="":
                        numtotalVotes = int(review[3])

                    weightMaxHelpVotes = 0

                    if numtotalVotes >= 0 and numtotalVotes <10:
                        weightMaxHelpVotes = 0
                    elif numtotalVotes >= 10 and numtotalVotes <200:
                        weightMaxHelpVotes = float(float(numHelpful)/float(numtotalVotes))
                    else:
                        weightMaxHelpVotes = 1.5*float(float(numHelpful)/float(numtotalVotes))

                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    if len(datesplit)>1 and datesplit[1]!=' ' and len(datesplit[1])<=5:
                        year = int(datesplit[1])
                        month = int(month)
                        day = int(day)
                        currentDay = datetime(year, month, day)

                        productDates.append((currentDay))
                        if currentDay >maxDate:
                            maxDate = currentDay
                        if currentDay <minDate:
                            minDate = currentDay

                        reviewPolarity = ComputeReviewPolarity(review[6],category)
                        SentiFile.write(review[0])
                        SentiFile.write("\t")
                        SentiFile.write(str(reviewPolarity))
                        SentiFile.write("\n")
                        rates.append(reviewPolarity)
                        reviewHelpfulWeight.append(weightMaxHelpVotes)



                newweights = []
                index = 0
                #print("-------------------------------------------------")
                dayweights = []
                credweights = []
                upper = 0
                down1 = 0
                down2 = 0
                temp = 0
                for currentDay in productDates:
                    timeDiff = (currentDay-minDate).days
                    beta = 0.001
                    part1 = beta*timeDiff
                    part1 = part1 + 5
                    expValue = (math.e** part1 )
                    #print(rates[index])
                    #print(expValue)
                    #print(reviewHelpfulWeight[index])
                    #print("-------------------------------------------------")
                    upper = upper + reviewHelpfulWeight[index]*expValue*rates[index]
                    down1 = down1 + reviewHelpfulWeight[index]
                    down2 = down2 + expValue
                    temp = temp + reviewHelpfulWeight[index]*expValue
                    #newweights.append(finalReviewRate)
                    index = index + 1

                '''for item in newweights:
                  newFinalRate = newFinalRate + item
                  print(newFinalRate)
                  index = index + 1
                print("final count")
                print(newFinalRate)
                '''
                #print(upper)
                #print(down1)
                #print(down2)
                #print(down1*down2)
                #print(temp)
                if down1*down1>0:
                    newFinalRate = upper/down1*down2
                else:
                    newFinalRate = 0
                #print(newFinalRate)
                products.append(productId)
                previousWeights.append(newFinalRate)
                #print(productId)

           except IOError as e:
              pass

    index = 0
    for product in products:
        #print("product")
        #print(product)
        filehandle.write(product)
        filehandle.write("\t")
        #newFinalRate = ((float(previousWeights[index]) -minVal)/(float(maxVal-minVal)))*5
        newFinalRate = previousWeights[index]
        filehandle.write(str(newFinalRate))
        filehandle.write("\n")
        index = index + 1

    filehandle.close()
    SentiFile.close()
    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)

    return
def computeRateNumVotesDates(filePath,category,destDirectory):
    print("Procedure to compute product rate per category based on 0.5 NumVotes and 0.5 date freshness")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    filePathExpertiese = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategory/"+category+".txt"
    userExpert = dict()
    with open(filePathExpertiese, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        userExpert[row[0]] = int(row[1])

    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           productId = row[0]
           productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
           overallRate = 0
           counter = 0
           overallRateVotes = 0
           minDate = datetime(2050, 12, 31)
           maxDate = datetime(1950, 1, 1)
           productDates = []
           productRates = []
           try:
              with open(productFileName, 'r') as filep:
                #get the most recent date and oldest date
                for item in filep:
                    review = item.split('\t')
                    productRates.append(float(review[5]))
                    datesplit = review[2].split(',')
                    monthDay = datesplit[0]
                    month = ""
                    day = ""
                    monthDone = 0
                    for char in monthDay:
                        if char != " " and monthDone== 0:
                            month = month + char
                        if char == " ":
                            monthDone = 1
                        if monthDone== 1:
                            day = day + char

                    year = int(datesplit[1])
                    month = int(month)
                    day = int(day)

                    currentDay = datetime(year, month, day)
                    productDates.append((currentDay))
                    if currentDay >maxDate:
                        maxDate = currentDay
                    if currentDay <minDate:
                        minDate = currentDay

                    maxVotes = 0
                    try:
                        maxVotes = userExpert[review[0]]

                    except KeyError as e:
                        maxVotes = 0
                    numHelpful = int(review[4])
                    weight = 0
                    if maxVotes > 0:
                        weight = float(numHelpful/maxVotes)
                        overallRateVotes = overallRateVotes + weight*float(review[5])
                        counter = counter + 1
              overallRate = 0
              for i in range(len(productDates)):

                  up = (productDates[i]-minDate).days
                  up = float(up)
                  down = (maxDate-minDate).days
                  down = float(down)

                  dateFactor = float(up/down)
                  overallRate = overallRate + productRates[i]*dateFactor

              overallRate = overallRate/len(productDates)
              overallRate = round(overallRate,4)
              if counter > 0:
                  overallRateVotes = overallRateVotes/counter
              overallRateDates = overallRate
              finalRate = 0.5*overallRateVotes + 0.5*overallRateDates

              filehandle.write(productId)
              filehandle.write("\t")
              finalRate = round(finalRate,4)
              filehandle.write(str(finalRate))
              filehandle.write("\n")
           except IOError as e:
              pass

    filehandle.close()

    Finished = datetime.now()
    done = Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
import os
def computeTrueRateForAllCategoreis(directory,option,destDirectory,startFrom):
    print("Procedure to read Compute all product categories majority vote")
    print("Started")
    start = datetime.now()
    index = 0
    #endAt = startFrom + 4
    print(start)
    for filename in os.listdir (directory):
        if index >= startFrom:
            path = directory +filename
            category = filename
            categoryName = category.split(".txt")
            categoryName = categoryName[0]
            if option == 0:#Normal Mean
                computeMajorityVoteForProductCategories(path,categoryName)
            elif option == 1:#Weighted Mean NumVotes
                computeMajorityVoteForProductCategoriesWithUserExpert(path,categoryName,destDirectory)
            elif option == 2:#Weighted Mean Date Freshness
                computeMajorityVoteForProductCategoriesDateFreshness(path,categoryName,destDirectory)
            elif option == 3:#Weighted Mean 0.5 NumVotes and 0.5 Date Freshness
                computeRateNumVotesDates(path,categoryName,destDirectory)
            elif option == 4:#Adjusted Weighted Mean NumVotes
                computeMajorityVoteForProductCategoriesWithUserExpertAdjusted(path,categoryName,destDirectory)
            elif option == 10:#test Weighted Mean NumVotes
                computeMajorityVoteForProductCategoriesWithUserExpertTest(path,categoryName,destDirectory)
            elif option == 11:#Weighted Mean Date Freshness adjusted
                computeMajorityVoteForProductCategoriesDateFreshnessAdjusted(path,categoryName,destDirectory)
            elif option == 12:#Weighted Mean 0.5 NumVotes and 0.5 Date Freshness Adjusted
                computeRateNumVotesDatesAdjusted(path,categoryName,destDirectory)
            elif option == 13:#Weighted exponential Num Votes and Dates
                computeRateNumVotesDatesExponential(path,categoryName,destDirectory)
            elif option == 14:#Computing Baseline from previous paper
                computeRankForBaseline(path,categoryName,destDirectory)
        #if endAt == index:
           # break
        index = index + 1

    Finished = datetime.now()
    done = Finished - start
    print("Finished")
    print(Finished)
    print("done")
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
def sortRatedCategories(directory,destDirectory,startFrom):
    print("Procedure to sort categories after rating")
    print("Started")
    start = datetime.now()
    index = 0
    #endAt = startFrom + 4
    print(start)
    for filename in os.listdir (directory):
        if index >= startFrom:
            path = directory +filename
            category = filename
            categoryName = category.split(".txt")
            categoryName = categoryName[0]
            sortRatedCategory(path,categoryName,destDirectory)
        #if endAt == index:
         #   break
        index = index + 1

    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    print("done")
    return
from alogrithms import *
def sortRatedCategory(filePath,category,destDirectory):
    print("Procedure to read category rated File, get a product from it and read its file and sort it and write to a file for a cetegory file")
    #category = "Prime Pantry"
    #filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_weighted_date_vote_expo_test/Prime Pantry.txt"
    #category = "Books"
    #filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_weighted_date_vote_expo_test/Books.txt"
    print("Considering "+category)
    #product_Id Category sales_rank
    import sys
    sys.setrecursionlimit(100000)

    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    listofProducts = []
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         listofProducts.append((tuple[0],float(tuple[1])))

    quickSort(listofProducts)

    for item in reversed(listofProducts):
        filehandle.write(item[0])
        filehandle.write("\t")
        filehandle.write(str(item[1]))
        filehandle.write("\n")
    filehandle.close()
    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    print("done")
    return
def measureDistanceBetweenSalesRankandMajorityVote(directorySales,directory_Majority,destDirectory,startFrom):
    print("Procedure to measure differences in sales sorted lists and majority vote sorted lists")
    print("Started")
    start = datetime.now()
    print(start)
    index = 0
    #endAt = startFrom + 4
    for filename in os.listdir (directorySales):
        if index >= startFrom:
            path1 = directorySales +filename
            path2 = directory_Majority +filename
            category = filename
            categoryName = category.split(".txt")
            categoryName = categoryName[0]
            measureDistanceBetweenForCategory(path1,path2,categoryName,destDirectory)
        #if endAt == index:
         #   break
        index = index + 1


    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    print("done")
    return

    return
def measureDistanceBetweenForCategory(path1,path2,category,destDirectory):
    print("Procedure to compare two categories")
    #category = "Prime Pantry"
    #path1 = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_sales_rank/Prime Pantry.txt"
    #path2 = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_weighted_date_vote_expo_test/Prime Pantry.txt"
    #category = "Books"
    #path1 = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_sales_rank/Books.txt"
    #path2 = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_weighted_date_vote_expo_test/Books.txt"
    print("Considering "+category)
    #product_Id Category sales_rank
    import sys
    sys.setrecursionlimit(100000)
    print("Started")
    start = datetime.now()
    print(start)
    line = ""
    salesRankList = []
    majorityVoateList = []
    filehandle = open(destDirectory+category+".txt",'a')
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         salesRankList.append(tuple[0])

    with open(path2, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         majorityVoateList.append(tuple[0])

    print(len(majorityVoateList))
    print(len(salesRankList))
    salesRankIndices = []
    majorityIndices = []
    if len(salesRankList) != len(majorityVoateList):
       print("Error UnEven Lists")
       return
    else:
        salesIndex = 0
        for sales in (salesRankList):


            majorIndex = 0
            for majority in (majorityVoateList):
                if sales == majority:
                    difference = salesIndex - majorIndex
                    majorityIndices.append(majorIndex)
                    salesRankIndices.append(salesIndex)
                    #filehandle.write(sales)
                    #filehandle.write("\t")
                    #filehandle.write(str(difference))
                    #filehandle.write("\n")
                    break
                majorIndex = majorIndex + 1
            salesIndex = salesIndex + 1
    #filehandle.close()

    print(len(majorityIndices))
    print(len(salesRankIndices))
    for i in range(len(salesRankIndices)):
        filehandle.write(str(salesRankIndices[i]))
        filehandle.write("\t")
        filehandle.write(str(majorityIndices[i]))
        filehandle.write("\n")

    filehandle.close()

    Finished = datetime.now()
    done = Finished - start
    #print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    print("Finished")
    print(Finished)
    print("done")
    return
def computeOverandUnderRating(directory):
    print("Started")
    start = datetime.now()
    print(start)
    for filename in os.listdir (directory):
        path1 = directory + "\\"+filename
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        computeOverandUnderRatingForCategory(path1,categoryName)
        #print("-----------------------------------------------------")

    print("Done")
    return
def computeOverandUnderRatingForCategory(path1,category):

    line = ""
    productList = []
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         productList.append(int(tuple[1]))

    numValues = len(productList)
    numOverRated = 0
    numUnderRated = 0
    numTrueRated = 0
    for item in productList:
        if item > 0:
            numOverRated = numOverRated + 1
        elif item < 0:
            numUnderRated = numUnderRated + 1
        else:
            numTrueRated = numTrueRated + 1


    numOverRated = float(float(numOverRated)/numValues)
    numUnderRated = float(float(numUnderRated)/numValues)
    numTrueRated = float(float(numTrueRated)/numValues)

    print(category+ "\t"+str(round(numOverRated,3)*100) +"\t"+str(round(numUnderRated,3)*100)+"\t"+str(round(numTrueRated,3)*100))

    return
def getMinMAxNumVotesForEachReviewerForAllCategories(directory):
    print("Started")
    start = datetime.now()
    print(start)
    for filename in os.listdir (directory):
        path1 = directory + "\\"+filename
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        getMinMAxNumVotesForEachReviewerPerCategory(path1,categoryName)


    print("Done")
    return

def getHelpfulVotesForEachReviewerForAllCategories(directory):
    print("Started getHelpfulVotesForEachReviewerForAllCategories ")
    start = datetime.now()
    print(start)
    for filename in os.listdir (directory):
        path1 = directory + "/"+filename
        print("path1")
        print(path1)
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        getHelpfulVotesForEachReviewerPerCategory(path1,categoryName)

    print("Done")
    return
def getNumReviewsForAllCategories(directory):
    print("Started getNumReviewsPerCategory ")
    start = datetime.now()
    print(start)
    for filename in os.listdir (directory):
        path1 = directory + "/"+filename
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        getNumReviewsPerCategory(path1,categoryName)

    print("Done")
    return
def getNumReviewsPerCategory(path1,category):
    line = ""
    product = ""
    print("Started getNumReviewsPerCategory")
    print("Considering "+category)
    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/NumRewviewsPerCategory/"+category+".txt",'a')
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         product = tuple[0]
         productFilePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+product+".txt"
         numReviews = 0
         with open(productFilePath, 'r') as productfp:
            for reviewline in productfp:
                numReviews= numReviews + 1

         filehandle.write(product)
         filehandle.write('\t')
         filehandle.write(str(numReviews))
         filehandle.write('\n')

    filehandle.close()
    print("Done ")
    return
def getNumvotesDistributionForAllCategories(directory):
    print("Started getNumReviewsPerCategory ")
    start = datetime.now()
    print(start)
    distributions = [(0,0),(1,10),(11,30),(31,50),(51,80),(81,300),(301,500),(501,1000),(1001,100000)]
    print(distributions)
    for filename in os.listdir (directory):
        path1 = directory + "/"+filename
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        getNumvotesDistributionForPerCategory(path1,categoryName)

    print("Done")
    return
def getNumvotesDistributionForPerCategory(path1,category):
    line = ""
    product = ""
    userHelpful = dict()
    print("Considering "+category)
    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/NumVotesDistribution/"+category+".txt",'a')
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         product = tuple[0]

         productFilePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+product+".txt"

         with open(productFilePath, 'r') as productfp:
            for reviewline in productfp:
                review = reviewline.split('\t')
                try:
                    reviewVotes = userHelpful[review[4]]
                    reviewVotes = reviewVotes + 1
                    userHelpful[review[4]] = reviewVotes
                except KeyError as e:
                    userHelpful[review[4]] = 1
    '''
    maxNum = -1000
    for key,value in userHelpful.items():
      #print(str(key)+" "+str(value))
      if maxNum < int(key):
          maxNum = int(key)
    for i in range(10):
        distributions[i] = i + i*maxNum
    '''
    distributions = [(0,0),(1,10),(11,30),(31,50),(51,80),(81,300),(301,500),(501,1000),(1001,100000)]
    values = [0,0,0,0,0,0,0,0,0,0]
    for key,value in userHelpful.items():
        ke = int(key)
        innnerIndex = 0
        for dist in distributions:
            if ke >= dist[0] and ke <=dist[1]:
                values[innnerIndex] = values[innnerIndex] + int(value)
                break
            innnerIndex = innnerIndex + 1
    allStr = ""
    for val in values:
        filehandle.write(str(val))
        filehandle.write('\n')
        allStr = allStr + " " + str(val)
    print(allStr)

    filehandle.close()
    print("Done ")
    return
def getNumHelpvotesDistributionForAllCategoriesUsers(directory):
    print("Started getNumHelpvotesDistributionForAllCategoriesUsers ")
    start = datetime.now()
    print(start)
    distributions = [(0,0),(1,5),(6,10),(11,15),(16,20),(21,25),(26,30),(31,40),(41,100000)]
    print(distributions)
    for filename in os.listdir (directory):
        path1 = directory + "/"+filename
        category = filename
        categoryName = category.split(".txt")
        categoryName = categoryName[0]
        getNumHelpvotesDistributionPerCategoriesUsers(path1,categoryName)

    print("Done")
    return
def getNumHelpvotesDistributionPerCategoriesUsers(path1,category):
    line = ""
    product = ""
    userHelpful = dict()
    print("Considering "+category)
    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/HelpfulVotesDistribution/"+category+".txt",'a')



    with open(path1, 'r') as productfp:
        for reviewline in productfp:
            review = reviewline.split('\t')
            try:
                reviewVotes = userHelpful[review[1]]
                reviewVotes = reviewVotes + 1
                userHelpful[review[1]] = reviewVotes
            except KeyError as e:
                userHelpful[review[1]] = 1

    distributions = [(0,0),(1,5),(6,10),(11,15),(16,20),(21,25),(26,30),(31,40),(41,100000)]
    values = [0,0,0,0,0,0,0,0,0,0]
    for key,value in userHelpful.items():
        ke = int(key)
        innnerIndex = 0
        for dist in distributions:
            if ke >= dist[0] and ke <=dist[1]:
                values[innnerIndex] = values[innnerIndex] + int(value)
                break
            innnerIndex = innnerIndex + 1
    allStr = ""
    for val in values:
        filehandle.write(str(val))
        filehandle.write('\n')
        allStr = allStr + " " + str(val)
    print(allStr)

    filehandle.close()
    return
def getHelpfulVotesForEachReviewerPerCategory(path1,category):
    line = ""
    product = ""
    print("Started getHelpfulVotesForEachReviewerPerCategory")
    print("Considering "+category)
    userHelpful = dict()
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         product = tuple[0]
         productFilePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+product+".txt"
         with open(productFilePath, 'r') as productfp:
            for reviewline in productfp:
                review = reviewline.split('\t')
                try:
                    reviewVotes = userHelpful[review[0]]
                    reviewVotes[0] = int(reviewVotes[0]) + int(review[4])
                    reviewVotes[1] = int(reviewVotes[1]) + int(review[3])
                    userHelpful[review[0]] = reviewVotes
                except KeyError as e:
                    userHelpful[review[0]] = list((review[4],review[3]))

    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/"+category+".txt",'a')
    #write the following form
    #UserID NumHelpfulVotes TotalNumVotes NumHelpfulVotes/TotalNumVotes
    for key,value in userHelpful.items():
        filehandle.write(key)
        filehandle.write('\t')
        filehandle.write(str(value[0]))
        filehandle.write('\t')
        filehandle.write(str(value[1]))
        filehandle.write('\t')
        if int(value[1]) > 0:
            filehandle.write(str(float(float(value[0])/float(value[1]))))
        else:
            filehandle.write("0")
        filehandle.write('\n')
    print("Num Users Per Category")
    print(len(userHelpful))
    return
def getMinMAxNumVotesForEachReviewerPerCategory(path1,category):
    line = ""
    product = ""
    print("Started getHelpfulVotesForEachReviewerPerCategory")
    print("Considering "+category)
    userHelpful = dict()
    with open(path1, 'r') as fp:
      for line in fp:
         tuple = line.split('\t')
         product = tuple[0]
         productFilePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+product+".txt"
         with open(productFilePath, 'r') as productfp:
            for reviewline in productfp:
                review = reviewline.split('\t')
                try:
                    helpful = userHelpful[review[0]]
                    if int(helpful) < int(review[4]):
                        userHelpful[review[0]] = review[4]
                except KeyError as e:
                    userHelpful[review[0]] = review[4]

    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/"+category+".txt",'a')
    for key,value in userHelpful.items():
        filehandle.write(key)
        filehandle.write('\t')
        filehandle.write(value)
        filehandle.write('\n')
    print("Num Users Per Category")
    print(len(userHelpful))
    return
    return
def countNumberOFGoodVotesForUsersPerCategory():

    directory = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategory/"
    for filename in os.listdir (directory):
        path1 = directory +filename
        category = filename
        categoryName = category.split(".txt")
        #print("considering "+categoryName[0])
        totalNumofUsers = 0
        totalNumOfUsersZero = 0
        with open(path1, 'r') as fp:
          for line in fp:
            row = line.split('\t')
            maxNum =  int(row[1])
            if maxNum == 0:
                totalNumOfUsersZero = totalNumOfUsersZero +1
            totalNumofUsers = totalNumofUsers + 1
        print(str(totalNumofUsers))
    return
import re
def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''

    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

def ComputeReviewPolarity(text,category):

    if category == "Arts, Crafts & Sewing":
        category = "Arts"
    if category == "Camera &amp; Photo":
        category = "Camera"
    if category == "Cell Phones & Accessories":
        category = "Cell"
    if category == "Computers & Accessories":
        category = "Computers"
    if category == "Gift Cards Store":
        category = "Gift"
    if category == "Grocery & Gourmet Food":
        category = "Grocery"
    if category == "Health & Personal Care":
        category = "Health"
    if category == "Home &amp; Kitchen":
        category = "HomeKitchen"
    if category == "Home Improvement":
        category = "HomeImprovement"
    if category == "Industrial & Scientific":
        category = "Industrial"
    if category == "Kitchen & Dining":
        category = "Kitchen"
    if category == "Movies & TV":
        category = "Movies"
    if category == "Musical Instruments":
        category = "MusicalInstruments"
    if category == "Office Products":
        category = "OfficeProducts"
    if category == "Patio, Lawn & Garden":
        category = "Patio"
    if category == "Pet Supplies":
        category = "PetSupplies"
    if category == "Prime Pantry":
        category = "Prime"
    if category == "Sports &amp; Outdoors":
        category = "Sports"
    if category == "Toys & Games":
        category = "Toys"
    if category == "Toys & Games":
        category = "Toys"
    if category == "Video Games":
        category = "VideoGames"

    inputFile = "/research/remote/petabyte/users/yassien/Truth_rating_code/temp/"+category+"/test.txt"
    filehandle = open(inputFile,'a')
    sentences = splitParagraphIntoSentences(text)
    for sent in sentences:
        filehandle.write(sent)
        filehandle.write("\n")
    filehandle.close()

    command = "java -jar SentiStrengthCom.jar sentidata /research/remote/petabyte/users/yassien/Truth_rating_code/SentStrength_Data_Sept2011/ input "+inputFile
    os.system(command)
    fileToRead = "/research/remote/petabyte/users/yassien/Truth_rating_code/temp/"+category+"/test0_out.txt"

    commentPolarity = 0
    with open(fileToRead, 'r') as sentiStrfp:
        bIgnoreFirst = 0
        for senti in sentiStrfp:
           if bIgnoreFirst == 0:
               bIgnoreFirst = 1
               continue
           sentSplit = senti.split('\t')
           numPostive = int(sentSplit[0])
           numNegative = int(sentSplit[1])
           sentPolarity = numPostive+numNegative
           if sentPolarity >=0:
               commentPolarity = commentPolarity + 1
           else:
               commentPolarity = commentPolarity - 1

    os.remove(inputFile)
    os.remove(fileToRead)

    return commentPolarity
#------------------------------------Program Starts Here-----------------------------------------------------------------
#countNumberofVotesFromFolder("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_10M_Not_Finished")
from analysis import getProductsWithNumberofReviewsThreshold

#readDataStanfordDataSetTechniqueTwo("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/aggressive_dedup.json/aggressive_dedup.json.gz2",0)
#getProductsWithNumberofReviewsThreshold("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_two/","C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/numProductReviews.txt",20)
#from analysis import *

#readDataStanfordDataSetTechniqueOne()
#readDataStanfordDataSetTechniqueThree("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/aggressive_dedup.json/aggressive_dedup.json.gz2")

#------------------------------------------------old--------------------------------------------------------------------

#readMetaDataFileAndWriteOnlyNeeded("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/metadata.json/metadata.json")
#createNewMetaDataWithOnlySalesRank("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/metadata.json/MetaDataSet.txt")
#readSalesRankMetaDataFile("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/metadata.json/Metadata_Sales_Rank.txt")

#createSmallerDatasSetFile("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/aggressive_dedup.json/aggressive_dedup.json.gz2")

#retrieveProductReviewsPerProduct("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews\Unique_Products_Stanford_three/aggressive_dedup_smaller.txt")

#readSalesRankMetaAndCreateFilesWithCategories("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews\metadata.json\Metadata_Sales_Rank.txt")

#computeMajorityVoteForAllProductCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories",0)

#sortRatedCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories")

#measureDistanceBetweenSalesRankandMajorityVote("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories_sorted_sales_rank","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories_sorted")

#computeOverandUnderRating("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories_differences")

#getMinMAxNumVotesForEachReviewerForAllCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three\categories")

#------------------------------------Experiment Start
#This is the date Experiment
#computeMajorityVoteForProductCategoriesDateFreshness("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/Books.txt","Books","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_weighted_date_rating/")
'''
computeTrueRateForAllCategoreis("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/",11,"/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_weighted_date_adjusted_rating/")

sortRatedCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_weighted_date_adjusted_rating/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_weighted_date_adjusted/")

measureDistanceBetweenSalesRankandMajorityVote("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_sales_rank/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_weighted_date_adjusted/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_differences_wegighted_date_adjusted_R/")

'''
#This is 0.5 date and 0.5 UserVote
#countNumberOFGoodVotesForUsersPerCategory()

#startFrom = int(raw_input("Start where "))

#computeTrueRateForAllCategoreis("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/",13,"/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_exp_date_only/",startFrom)

#sortRatedCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_exp_date_only/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_exp_date_only/",startFrom)

#measureDistanceBetweenSalesRankandMajorityVote("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_sales_rank/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_exp_date_only/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_differences_exp_date_only_R/",startFrom)

#getHelpfulVotesForEachReviewerForAllCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories")

#getNumReviewsForAllCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories")

#getNumHelpvotesDistributionForAllCategoriesUsers("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/")

'''
directory = "" "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"
numProducts = 0
for filename in os.listdir (directory):
    numProducts = numProducts + 1

print("Num Products")
print(numProducts)

totalVotes = 0
helpfulVotes = 0
directory = "" "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/"
for filename in os.listdir (directory):
    filePath = directory+"/"+filename
    totalVotes = 0
    helpfulVotes = 0
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           if row[2] != "":
            totalVotes = totalVotes + int(row[2])
            helpfulVotes = helpfulVotes + int(row[1])
    print(str(totalVotes) + "\t"+str(helpfulVotes))
    filePath= "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_Baseline/Beauty.txt"
newBeauty = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_Baseline/NewBeauty.txt",'a')
wri = 1
with open(filePath, 'r') as fp:
      for line in fp:
       if wri == 1:
           newBeauty.write(line)
           wri = 0
       elif wri == 0:
           wri = 1
           continue
print("Finished Writing New File")
'''
'''
directory = "" "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"
index = 0
print("Hi begin")
for filename in os.listdir (directory):
        filePath = directory+filename
        num5 = 0
        num4 = 0
        num3 = 0
        num2 = 0
        num1 = 0
        if index == 10:
            break
        with open(filePath, 'r') as fp:
            for line in fp:
                row = line.split('\t')
                if row[5] != "":
                    rate = float(row[5])
                    if rate == 5.0:
                        num5 = num5 + 1
                    if rate == 4.0:
                        num4 = num4 + 1
                    if rate == 3.0:
                        num3 = num3 + 1
                    if rate == 2.0:
                        num2 = num2 + 1
                    if rate == 1.0:
                        num1 = num1 + 1
        print(str(num5)+"\t"+str(num4)+"\t"+str(num3)+"\t"+str(num2)+"\t"+str(num1)+"\t")
        index = index + 1
        '''
'''
directory = "" "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_std/"
ranges = [0,0,0,0,0] #0-0.5-1-1.5-2
numpro = 0
for filename in os.listdir (directory):
    filePath = directory+"/"+filename
    sumPerCat = 0
    with open(filePath, 'r') as fp:
      for line in fp:
           row = line.split('\t')
           std = float(row[0])
           numpro = numpro + 1
           sumPerCat = sumPerCat + 1
           if std <0.5:
               ranges[0] = ranges[0] + 1
           elif std >=0.5 and std <1:
               ranges[1] = ranges[1] + 1
           elif std >=1 and std <1.5:
               ranges[2] = ranges[2] + 1
           elif std >=1.5 and std <2:
               ranges[3] = ranges[3] + 1
           elif std >=2:
               ranges[4] = ranges[4] + 1
    #print("sumPerCat")
    #print(sumPerCat)
#print("numpro")
#print(numpro)
sum = 0
for range in ranges:
    print(range)
    sum = sum + range
#print("Sum Products")
#print(sum)
'''
def computeUserExpertieseForCategores():
    directory = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/"
    userCrid = dict()
    for filename in os.listdir (directory):
        filePath = directory+"/"+filename
        sumPerCat = 0
        print("Considering "+filename)
        with open(filePath, 'r') as fp:
          for line in fp:
            row = line.split('\t')
            userID = row[0]
            crid = float(row[3])
            try:
                expert = userCrid[userID]
                expert.append(crid)
                userCrid[userID] = expert
            except KeyError as e:
                expert = []
                expert.append(crid)
                userCrid[userID] = expert
    print("Done calculation")
    filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserCridibility.txt",'a')
    print("Start writing")
    for key,value in userCrid.items():
        filehandle.write(key)
        filehandle.write("\t")
        for cri in value:
            filehandle.write(str(cri))
            filehandle.write("\t")
        filehandle.write("\n")
    filehandle.close()

    print("Done writing")
    return
filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/Computers & Accessories.txt"
userList = []
with open(filePath, 'r') as fp:
          for line in fp:
            row = line.split('\t')
            rate = float(row[3])
            if rate == 1.0:
                userList.append(row[0])
print("userList")
print(len(userList))
filePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/Computers & Accessories.txt"
rates = []
filehandle = open("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/TopCatUserRating.txt",'a')
with open(filePath, 'r') as fp:
          for line in fp:
            row = line.split('\t')
            productId = row[0]
            productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
            with open(productFileName, 'r') as filep:
                for line in filep:
                    rev = line.split('\t')
                    user = rev[0]
                    for usr in userList:
                        if usr == user:
                            rates.append((rev[1],float(rev[5])))
                            filehandle.write(user)
                            filehandle.write("\t")
                            filehandle.write(rev[1])
                            filehandle.write("\t")
                            filehandle.write(rev[5])
                            filehandle.write("\n")
print("rates")
print(len(rates))
filehandle.close()