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
                    part3 = part1+ part2
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
def computeStdForCategory(filePath,category,destDirectory):
    print("Procedure to compute Std for Category")
    print("Considering "+category)
    print("Started")
    start = datetime.now()
    print(start)
    filehandle = open(destDirectory+category+".txt",'a')
    with open(filePath, 'r') as fp:
      for line in fp:
        row = line.split('\t')
        productId = row[0]
        productFileName = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+productId+".txt"
        rates = []
        try:
              with open(productFileName, 'r') as filep:
                sum = 0
                for item in filep:
                    review = item.split('\t')
                    rates.append(float(review[5]))
                    sum = sum + float(review[5])
                nNum = len(rates)
                mean = sum/nNum
                sum_deviation = 0
                for rate in rates:
                    sum_deviation = sum_deviation + ((rate-mean)*(rate-mean))
                std = (sum_deviation/nNum)**(0.5)
                filehandle.write(str(std))
                filehandle.write("\n")
        except IOError as e:
              pass
    filehandle.close()
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
           comments = []
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

                        comments.append(review[6])
                        reviewHelpfulWeight.append(weightMaxHelpVotes)

                rates = ComputeReviewPolarity(comments,category,SentiFile)
                newweights = []
                index = 0
                upper = 0
                down1 = 0
                down2 = 0
                temp = 0
                revHelpLen = len(reviewHelpfulWeight)
                ratLen = len(reviewHelpfulWeight)
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
                    revHelWeight = 0.01
                    sentWeg = 0.01
                    if index < revHelpLen:
                        revHelWeight = reviewHelpfulWeight[index]
                    if index < ratLen:
                        sentWeg = rates[index]
                    upper = upper + revHelWeight*expValue*sentWeg
                    down1 = down1 + revHelWeight
                    down2 = down2 + expValue
                    temp = temp + revHelWeight*expValue
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
            elif option == 15:#compute Std for all
                computeStdForCategory(path,categoryName,destDirectory)

        #if index == (endAt-1):
         #   break
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
    print("Started ")
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
        #if index == (endAt-1):
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
    if len(listofProducts) == 0:
        print("problem with zero lists")
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

        #if index == (endAt-1):
           # break
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

    salesRankIndices = []
    majorityIndices = []
    if len(salesRankList) != len(majorityVoateList):
       print("Error UnEven Lists")
       return
    else:
        salesIndex = 0
        for sales in (salesRankList):
            salesRankIndices.append(salesIndex)

            majorIndex = 0
            for majority in (majorityVoateList):
                if sales == majority:
                    difference = salesIndex - majorIndex
                    majorityIndices.append(majorIndex)
                    #filehandle.write(sales)
                    #filehandle.write("\t")
                    #filehandle.write(str(difference))
                    #filehandle.write("\n")
                    break
                majorIndex = majorIndex + 1
            salesIndex = salesIndex + 1
    #filehandle.close()



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

def ComputeReviewPolarity(reviews,category,SentiFile):

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

    for review in reviews:
        counter = 0
        sentences = splitParagraphIntoSentences(review)
        for sent in sentences:
            filehandle.write(sent)
            filehandle.write("\n")
        filehandle.write("---")
        filehandle.write("\n")
    filehandle.close()

    command = "java -jar SentiStrengthCom.jar sentidata /research/remote/petabyte/users/yassien/Truth_rating_code/SentStrength_Data_Sept2011/ input "+inputFile
    os.system(command)
    fileToRead = "/research/remote/petabyte/users/yassien/Truth_rating_code/temp/"+category+"/test0_out.txt"

    finalPolarity = []
    commentPolarity = 0
    index = 0
    innerIndex = 0
    with open(fileToRead, 'r') as sentiStrfp:
        bIgnoreFirst = 0
        for senti in sentiStrfp:
           if bIgnoreFirst == 0:
               bIgnoreFirst = 1
               continue
           sentSplit = senti.split('\t')
           if sentSplit[2] == "\n":
               continue

           numPostive = int(sentSplit[0])
           numNegative = int(sentSplit[1])
           sentPolarity = numPostive+numNegative
           if sentPolarity >=0:
               commentPolarity = commentPolarity + 1
           else:
               commentPolarity = commentPolarity - 1

           if sentSplit[2] == "---\n":
            finalPolarity.append(commentPolarity)
            SentiFile.write(str(commentPolarity))
            SentiFile.write("\n")
            commentPolarity = 0

    os.remove(inputFile)
    os.remove(fileToRead)

    return finalPolarity
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

'''file = "test.txt"
command = "java -jar SentiStrengthCom.jar sentidata /research/remote/petabyte/users/yassien/Truth_rating_code/SentStrength_Data_Sept2011/ input "+file
print("command")
print(command)
text = "This book is well written and very organized. The author did an excellent job of explaining a complicated subject and I was surprised at how easy it was to read. It was so interesting and informative that couldn't put the book down once I started to read it. I purchased four more books of different titles and read them with the same ease. It's not that the subject is any easy read but it was so clearly explained and flowed very nicely as it untangled many questions that I had concerning prophecy. I purchased this title for a friend of mine and highly recommend this book to anyone interested in Bible prophecy.	Excellent Read"
os.system(command)
 sent = str(s.strip())
    lisa = sent.split(' ')
    print("lisa")
    print(lisa)
    finalSent = ""
    for word in lisa:
        finalSent = finalSent + word+"+"
    print("finalSent")
    print(finalSent)

'''
'''
from bs4 import BeautifulSoup
import urllib3
file = "pop"
print(file)
http = urllib3.PoolManager()
soup = BeautifulSoup(http.urlopen('GET','http://www.bcsfootball.org').read())

import urllib.request
proxy_handler = urllib.request.ProxyHandler({"http": "http://bproxy.rmit.edu.au:8080"})
proxy_auth_handler = urllib.request.HTTPBasicAuthHandler()
print("Before Opener")
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
print("After Opener Before Open")
x = opener.open('https://www.google.com/')
print("After All Opening")
print(x.read())
'''
'''
from openamazon.openamazon import amazon
object=amazon()
results= object.search("soap")
for product in results:
    print (product['name'])   #This will print the product name
    print (product['price'])  #This will print the current price
    print (product['url'])    #This will print the product url
    print (product['reference_code']) #This will print the unique amazon reference code
'''


def product_details(url,productId):
    import urllib.request
    from bs4 import BeautifulSoup

    proxy_handler = urllib.request.ProxyHandler({"http": "http://bproxy.rmit.edu.au:8080"})
    proxy_auth_handler = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    product={}
    try:
        x = opener.open(url)

        print("AMAZON...product details")

        #-----------------------------------------------------------------------------
        soup=BeautifulSoup(x.read(),"html5lib")
        counter = 0
        for a in soup.find_all('a', href=True):
            extractedUrl = a['href']
            if productId in extractedUrl and "product-reviews" in extractedUrl:
                #print ("Found the URL:", a['href'])
                counter = counter + 1
        r1= soup.find(id="price")
        #print("counter")
        #print(counter)
        #-----------------------------------------------------------------------------
        mrp = None
        if r1 !=None:
            r2= r1.table.find_all("tr")
            mrp= r2[0].find_all("td")[1].text.strip()

        r3= soup.find(id="averageCustomerReviews")
        if(r3.find(id="acrPopover")):
            rating= r3.find(id="acrPopover")['title'].strip()[0]
        else:
            rating="0"
        if(r3.find(id="acrCustomerReviewText")):
            reviews= r3.find(id="acrCustomerReviewText").text.strip()[:-17]
        elif(r3.find(id="acrCustomerWriteReviewText")):
            reviews="0"
        else:
            reviews="not available"
        if(soup.find(id="altImages")):
            images=len(soup.find(id="altImages").find_all("li",{"class":"a-spacing-small item"}))
        else:
            images=0
        if(soup.find(id="productDescription")):
            description=soup.find(id="productDescription").find("div",{"class":"productDescriptionWrapper"}).text.strip()
        else:
            description="Not Available"
        product['mrp']=mrp
        product['reviews']=reviews
        product['images']=images
        product['rating']=rating
        product['description']=description

        numberVerified = 0
        numberID = 0
        numCommon = 0
        authorID = ""
        name = ""
        r1=soup.find_all("div",{"class":"a-row"})
        for x in range(0,len(r1)):
            r2=r1[x].find("span",{"class":"a-size-mini a-color-state a-text-bold"})
            r3=r1[x].find("a",{"class":"noTextDecoration"})
            verified = "Not Verified Purchase"
            if r2 != None:
                verified = r2.text.strip()
                numberVerified = numberVerified + 1
            if r3 != None:
                 idLink = r3['href']
                 parts = idLink.split("/")
                 authorID = parts[len(parts)-1]
                 name = r3.text.strip()
                 numberID = numberID + 1
            if r2 != None and r3 != None:
                numCommon = numCommon +1
            if authorID!="" and name !="":
                print(authorID +" "+name +" "+verified)
        print("Num Common")
        print(numCommon)
        print("Num Verified")
        print(numberVerified)
        print("Num ID")
        print(numberID)
    except urllib.error.HTTPError as e:
        print("Service Unavailable")
    print("....Done")
    return product


def extractVerifiedFromUrl(url,productUserVerification,browser):

    '''from fake_useragent import UserAgent
    ua = UserAgent()
    ua.ie
    '''
    import time
    import random
    import urllib.request
    from bs4 import BeautifulSoup
    proxy_handler = urllib.request.ProxyHandler({"http": "http://bproxy.rmit.edu.au:8080"})
    proxy_auth_handler = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    opener.addheaders = [('User-agent', browser)]
    result = 0
    try:
        x = opener.open(url)
        try:
            soup=BeautifulSoup(x.read(),"html5lib")
            authorID = ""
            name = ""
            r1=soup.find_all("div",{"class":"a-section review"})
            if len(r1)==0 :
                print("Could not load")
                result = -1
                time.sleep(5+(random.random()-0.5)*5)
                return productUserVerification, result
            for x in range(0,len(r1)):
                verified = "Not Verified Purchase"
                r2=r1[x].find_all("span",{"class":"a-size-mini a-color-state a-text-bold"})
                for y in r2:
                    verified = y.text.strip()
                r3=r1[x].find_all("a",{"class":"a-size-base a-link-normal author"})
                for y in r3:
                    res = str(y).split("profile")
                    res = res[1].split(">")
                    res = res[0].split("/")
                    res = res[1].split('"')
                    authorID =res[0]
                    name = y.text.strip()

                if authorID != "":
                    try:
                        availableString = productUserVerification[authorID+" "+name]
                        productUserVerification[authorID+" "+name] = verified
                    except KeyError as e:
                        productUserVerification[authorID+" "+name] = verified
        except urllib.error.HTTPError as e:
                print("Service Unavailable")
                print("Sleeping")
                result = -1
                time.sleep(50)
                return productUserVerification, result

    except urllib.error.HTTPError as e:
        print("Service Unavailable")
        result = -1
        time.sleep(20+(random.random()-0.5)*5)
    return productUserVerification, result

def getProductVerifiedPurchase(url,productId):
    '''
    proxy_handler = urllib.request.ProxyHandler({"http": "http://bproxy.rmit.edu.au:8080"})
    proxy_auth_handler = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    productUserVerification = dict()
    print("AMAZON...product verified Purchases")
    result = 0
    try:
        x = opener.open(url)
        soup=BeautifulSoup(x.read(),"html5lib")
        authorID = ""
        name = ""
        r1=soup.find_all("div",{"class":"a-section celwidget"})
        for x in range(0,len(r1)):
            verified = "Not Verified Purchase"
            r2=r1[x].find_all("span",{"class":"a-size-mini a-color-state a-text-bold"})
            for y in r2:
                res = str(y).split("\n")

                verified = res[1]
            r3=r1[x].find_all("a",{"class":"noTextDecoration"})
            for y in r3:
                res = str(y).split("profile")
                res = res[1].split(">")
                res = res[0].split("/")
                res = res[1].split('"')
                authorID =res[0]
                name = y.text.strip()

            if authorID != "":
                try:
                    availableString = productUserVerification[authorID+" "+name]
                    productUserVerification[authorID+" "+name] = verified
                except KeyError as e:
                    productUserVerification[authorID+" "+name] = verified
        '''
    import urllib.request
    from bs4 import BeautifulSoup
    productUserVerification = dict()
    result = -1
    previousCount = 0
    numRepition = 0
    externalRepition = 0
    for i in range(500):
        result = -1
        newUrl="http://www.amazon.com/product-reviews/"
        newUrl = newUrl + productId +"?pageNumber="+str(i)
        #newUrl="http://www.amazon.com/product-reviews/0001473123?pageNumber=2"
        numServiceUnAval = 0
        browserIndex = 0
        numRepition = 0
        browsers = ['Mozilla/5.0','Opera/9.80','Safari/537.36','Chrome/47.0.2526.111','AppleWebKit/537.36','Trident/7.0']
        while result == -1:
            if browserIndex > 5:
                browserIndex = 0
            productUserVerification, result = extractVerifiedFromUrl(newUrl,productUserVerification,browsers[browserIndex])
            if result == -1:
                numServiceUnAval = numServiceUnAval + 1
                browserIndex = browserIndex + 1
            if previousCount == len(productUserVerification):
                numRepition = numRepition + 1
            if previousCount != len(productUserVerification):
                previousCount = len(productUserVerification)
            if numRepition == 3:
                break

        if numRepition == 3:
            break
    return productUserVerification, result

#-----------------------------------------------------------------------------------------------------------------------
def crawlPorductVerification(productId,destDirectory):

    productUrl = "http://www.amazon.com/dp/"+productId
    print(productId)
    import urllib.request
    from bs4 import BeautifulSoup
    productUserVerification,result = getProductVerifiedPurchase(productUrl,productId)
    print(len(productUserVerification))
    if len(productUserVerification)>0:
        filePath = destDirectory+"/"+productId+".txt"
        filehandle = open(filePath,'w')
        for key,value in productUserVerification.items():
            try:
                string = str(key)+" "+str(value)+"\t"
                filehandle.write(string)
                if value == "Verified Purchase":
                    filehandle.write("1")
                else:
                    filehandle.write("0")
                filehandle.write("\n")
            except UnicodeEncodeError as e:
                pass
        filehandle.close();
    return
#-----------------------------------------------------------------------------------------------------------------------
def crawlDataForCategories(directory,startFrom,endAt):
    print("AMAZON...product verified Purchases")
    index = 0
    twohundredCounter = 0
    import time
    import urllib.request
    from bs4 import BeautifulSoup
    for filename in os.listdir (directory):
        categoryName = filename
        categoryName = categoryName.split(".txt")
        categoryName = categoryName[0]
        print("Considering "+categoryName)
        filePath = directory+filename
        destinationCat = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories_verified/"+categoryName
        if index >= startFrom:
            innnedIndex = 0
            with open(filePath, 'r') as fp:
                for line in fp:
                   if innnedIndex >= 3000:
                       productId = line.split("\t")
                       productId = productId[0]
                       crawlPorductVerification(productId,destinationCat)
                       if innnedIndex == endAt:
                             break
                       if twohundredCounter == 100:
                           print("Sleeping")
                           time.sleep(200)
                           twohundredCounter = 0
                       twohundredCounter = twohundredCounter + 1

                   innnedIndex = innnedIndex + 1
        index = index + 1


    print("......Done")
    return

def countNumberofProductsPerCategoryVerified(directory):
    for category in os.listdir (directory):
        path = directory +"/"+category
        counter = 0
        for filename in os.listdir (path):
            counter = counter + 1
        #print(category+" "+str(counter))
        print(str(counter))

    return
def countNumberofReviewsPerProductInVerified(directory):
    for category in os.listdir (directory):
        path = directory +"/"+category
        writePath = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_verified_differences/"
        fileToWrite = category + ".txt"
        print(fileToWrite)
        filehandle = open(writePath+fileToWrite,'a')
        for Product in os.listdir (path):
            productPath = path+"/"+Product
            countReviewsVerified = 0
            with open(productPath, 'r') as fp:
              for line in fp:
                countReviewsVerified = countReviewsVerified + 1

            productOriginalFile = "/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/Product_Reviews/"+Product
            countReviewsOriginal = 0
            with open(productOriginalFile, 'r') as fp:
              for line in fp:
                countReviewsOriginal = countReviewsOriginal + 1

            filehandle.write(Product)
            filehandle.write("\t")
            filehandle.write(str(countReviewsOriginal))
            filehandle.write("\t")
            filehandle.write(str(countReviewsVerified))
            filehandle.write("\n")

    return
def collectDataForCDFAnalysis(sourceDirectory,baseDirectory,destDirectory):
    print("Procedure to prepare data for CDF Analysis")
    print("Started")
    start = datetime.now()

    for filename in os.listdir (sourceDirectory):
            categoryPath = sourceDirectory +filename
            category = filename
            categoryName = category.split(".txt")
            categoryName = categoryName[0]
            print("Considering "+categoryName)
            filehandle = open(destDirectory+category+".txt",'w')
            with open(categoryPath, 'r') as fp:
              for line in fp:
                   row = line.split('\t')
                   productId = row[0]
                   fileName = baseDirectory+productId+".txt"
                   try:
                      with open(fileName, 'r') as filep:
                        for item in filep:
                            review = item.split('\t')
                            filehandle.write(review[5]) #Star Rating
                            filehandle.write("\t")
                            filehandle.write(review[2]) #Date
                            filehandle.write("\t")
                            numVotes = 0
                            if review[3]!="":
                                numVotes = float(review[3])
                            filehandle.write(review[3]) #All Votes
                            filehandle.write("\t")
                            helpfulVotes = 0
                            if review[4]!="":
                                helpfulVotes = float(review[4])
                            filehandle.write(review[4]) #Helpful Votes
                            filehandle.write("\t")
                            helpfulness  = 0
                            if numVotes != 0:
                                helpfulness = float(helpfulVotes/numVotes)
                            filehandle.write(str(helpfulness)) #Helpfulness
                            filehandle.write("\n")
                   except IOError as e:
                    pass
            filehandle.close()
    step2Finished = datetime.now()
    done = step2Finished - start
    print("Finished in "+str(round(done.total_seconds()/60,3))+" minutes")
    return
def readProduct(fileName):
    with open(fileName, 'r') as filep:
        for item in filep:
            review = item.split('\t')
            #print(review[5]) #Star Rating
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
            #print(currentDay)
    return
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
#startFrom = 0
#computeTrueRateForAllCategoreis("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories/",15,"/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_std/",startFrom)

#sortRatedCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_exp_date_vote_last/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_exp_date_vote_last/",startFrom)

#measureDistanceBetweenSalesRankandMajorityVote("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_sales_rank/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_sorted_exp_date_vote_last/","/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_differences_exp_date_vote_last_R/",startFrom)

#getHelpfulVotesForEachReviewerForAllCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories")

#getNumReviewsForAllCategories("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories")

#getNumHelpvotesDistributionForAllCategoriesUsers("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/UserHelpfulVotesPerCategoryNew/")



#-----------------------------------------------------------------------------------------------------------------------
#productId = "1614271046"
#crawlPorductVerification(productId,"C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories_verified/Appliances/")

#crawlDataForCategories("C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories/",31,30000)
#--------------------------------------------------------------------------------------------------------
#countNumberofProductsPerCategoryVerified("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_verified")

#countNumberofReviewsPerProductInVerified("/research/remote/petabyte/users/yassien/Unique_Products_Stanford_three/categories_verified")
sourceDirectory = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/categories/"
baseDirectory = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three/Product_Reviews/"
destDirectory = "C:\Yassien_RMIT PhD\Datasets\TruthDiscovery_Datasets\Web data Amazon reviews/Unique_Products_Stanford_three\Data_For_CDF_Analysis/"
#collectDataForCDFAnalysis(sourceDirectory,baseDirectory,destDirectory)
'''fileName = baseDirectory+"B000SB4O8U.txt"
#readProduct(fileName)
fileName = "c://temp.txt"
lista = []
count = 0

with open(fileName, 'r') as filep:
    for item in filep:
        lista.append(int(item))
        overallAverage = 0
        for rate in lista:
            overallAverage = overallAverage + rate
        overallAverage = overallAverage/len(lista)
        print(round(overallAverage,3))
'''