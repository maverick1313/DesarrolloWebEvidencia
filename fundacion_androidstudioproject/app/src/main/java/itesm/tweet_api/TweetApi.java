/*
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
/*
 * This code was generated by https://github.com/google/apis-client-generator/
 * (build: 2017-11-07 19:12:12 UTC)
 * on 2017-11-15 at 20:33:16 UTC 
 * Modify at your own risk.
 */

package itesm.tweet_api;
/**
 * Service definition for TweetApi (v1).
 *
 * <p>
 * tweet REST API
 * </p>
 *
 * <p>
 * For more information about this service, see the
 * <a href="" target="_blank">API Documentation</a>
 * </p>
 *
 * <p>
 * This service uses {@link TweetApiRequestInitializer} to initialize global parameters via its
 * {@link Builder}.
 * </p>
 *
 * @since 1.3
 * @author Google, Inc.
 */
@SuppressWarnings("javadoc")
public class TweetApi extends com.google.api.client.googleapis.services.json.AbstractGoogleJsonClient {

  // Note: Leave this static initializer at the top of the file.
  static {
    com.google.api.client.util.Preconditions.checkState(
        com.google.api.client.googleapis.GoogleUtils.MAJOR_VERSION == 1 &&
        com.google.api.client.googleapis.GoogleUtils.MINOR_VERSION >= 15,
        "You are currently running with version %s of google-api-client. " +
        "You need at least version 1.15 of google-api-client to run version " +
        "1.23.0 of the tweet_api library.", com.google.api.client.googleapis.GoogleUtils.VERSION);
  }

  /**
   * The default encoded root URL of the service. This is determined when the library is generated
   * and normally should not be changed.
   *
   * @since 1.7
   */
  //public static final String DEFAULT_ROOT_URL = "https://tweet-webtoken-api.appspot.com/_ah/api/";
  public static final String DEFAULT_ROOT_URL = "https://proyecto2-raulbarranco.appspot.com/_ah/api/";

  /**
   * The default encoded service path of the service. This is determined when the library is
   * generated and normally should not be changed.
   *
   * @since 1.7
   */
  public static final String DEFAULT_SERVICE_PATH = "tweet_api/v1/tweet/";

  /**
   * The default encoded batch path of the service. This is determined when the library is
   * generated and normally should not be changed.
   *
   * @since 1.23
   */
  public static final String DEFAULT_BATCH_PATH = "batch";

  /**
   * The default encoded base URL of the service. This is determined when the library is generated
   * and normally should not be changed.
   */
  public static final String DEFAULT_BASE_URL = DEFAULT_ROOT_URL + DEFAULT_SERVICE_PATH;

  /**
   * Constructor.
   *
   * <p>
   * Use {@link Builder} if you need to specify any of the optional parameters.
   * </p>
   *
   * @param transport HTTP transport, which should normally be:
   *        <ul>
   *        <li>Google App Engine:
   *        {@code com.google.api.client.extensions.appengine.http.UrlFetchTransport}</li>
   *        <li>Android: {@code newCompatibleTransport} from
   *        {@code com.google.api.client.extensions.android.http.AndroidHttp}</li>
   *        <li>Java: {@link com.google.api.client.googleapis.javanet.GoogleNetHttpTransport#newTrustedTransport()}
   *        </li>
   *        </ul>
   * @param jsonFactory JSON factory, which may be:
   *        <ul>
   *        <li>Jackson: {@code com.google.api.client.json.jackson2.JacksonFactory}</li>
   *        <li>Google GSON: {@code com.google.api.client.json.gson.GsonFactory}</li>
   *        <li>Android Honeycomb or higher:
   *        {@code com.google.api.client.extensions.android.json.AndroidJsonFactory}</li>
   *        </ul>
   * @param httpRequestInitializer HTTP request initializer or {@code null} for none
   * @since 1.7
   */
  public TweetApi(com.google.api.client.http.HttpTransport transport, com.google.api.client.json.JsonFactory jsonFactory,
      com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
    this(new Builder(transport, jsonFactory, httpRequestInitializer));
  }

  /**
   * @param builder builder
   */
  TweetApi(Builder builder) {
    super(builder);
  }

  @Override
  protected void initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest<?> httpClientRequest) throws java.io.IOException {
    super.initialize(httpClientRequest);
  }

  /**
   * An accessor for creating requests from the Tweet collection.
   *
   * <p>The typical use is:</p>
   * <pre>
   *   {@code TweetApi tweet_api = new TweetApi(...);}
   *   {@code TweetApi.Tweet.List request = tweet_api.tweet().list(parameters ...)}
   * </pre>
   *
   * @return the resource collection
   */
  public Tweet tweet() {
    return new Tweet();
  }

  /**
   * The "tweet" collection of methods.
   */
  public class Tweet {

    /**
     * Create a request for the method "tweet.delete".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link Delete#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesTokenKey}
     * @return the request
     */
    public Delete delete(itesm.tweet_api.model.MessagesTokenKey content) throws java.io.IOException {
      Delete result = new Delete(content);
      initialize(result);
      return result;
    }

    public class Delete extends TweetApiRequest<itesm.tweet_api.model.MessagesCodeMessage> {

      private static final String REST_PATH = "delete";

      /**
       * Create a request for the method "tweet.delete".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link Delete#execute()} method to invoke the remote operation.
       * <p> {@link
       * Delete#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)} must
       * be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesTokenKey}
       * @since 1.13
       */
      protected Delete(itesm.tweet_api.model.MessagesTokenKey content) {
        super(TweetApi.this, "POST", REST_PATH, content, itesm.tweet_api.model.MessagesCodeMessage.class);
      }

      @Override
      public Delete setAlt(java.lang.String alt) {
        return (Delete) super.setAlt(alt);
      }

      @Override
      public Delete setFields(java.lang.String fields) {
        return (Delete) super.setFields(fields);
      }

      @Override
      public Delete setKey(java.lang.String key) {
        return (Delete) super.setKey(key);
      }

      @Override
      public Delete setOauthToken(java.lang.String oauthToken) {
        return (Delete) super.setOauthToken(oauthToken);
      }

      @Override
      public Delete setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Delete) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Delete setQuotaUser(java.lang.String quotaUser) {
        return (Delete) super.setQuotaUser(quotaUser);
      }

      @Override
      public Delete setUserIp(java.lang.String userIp) {
        return (Delete) super.setUserIp(userIp);
      }

      @Override
      public Delete set(String parameterName, Object value) {
        return (Delete) super.set(parameterName, value);
      }
    }
    /**
     * Create a request for the method "tweet.get".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link Get#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesTokenKey}
     * @return the request
     */
    public Get get(itesm.tweet_api.model.MessagesTokenKey content) throws java.io.IOException {
      Get result = new Get(content);
      initialize(result);
      return result;
    }

    public class Get extends TweetApiRequest<itesm.tweet_api.model.MessagesTweetList> {

      private static final String REST_PATH = "get";

      /**
       * Create a request for the method "tweet.get".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link Get#execute()} method to invoke the remote operation. <p>
       * {@link Get#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)}
       * must be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesTokenKey}
       * @since 1.13
       */
      protected Get(itesm.tweet_api.model.MessagesTokenKey content) {
        super(TweetApi.this, "POST", REST_PATH, content, itesm.tweet_api.model.MessagesTweetList.class);
      }

      @Override
      public Get setAlt(java.lang.String alt) {
        return (Get) super.setAlt(alt);
      }

      @Override
      public Get setFields(java.lang.String fields) {
        return (Get) super.setFields(fields);
      }

      @Override
      public Get setKey(java.lang.String key) {
        return (Get) super.setKey(key);
      }

      @Override
      public Get setOauthToken(java.lang.String oauthToken) {
        return (Get) super.setOauthToken(oauthToken);
      }

      @Override
      public Get setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Get) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Get setQuotaUser(java.lang.String quotaUser) {
        return (Get) super.setQuotaUser(quotaUser);
      }

      @Override
      public Get setUserIp(java.lang.String userIp) {
        return (Get) super.setUserIp(userIp);
      }

      @Override
      public Get set(String parameterName, Object value) {
        return (Get) super.set(parameterName, value);
      }
    }
    /**
     * Create a request for the method "tweet.insert".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link Insert#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesTweetInput}
     * @return the request
     */
    public Insert insert(itesm.tweet_api.model.MessagesTweetInput content) throws java.io.IOException {
      Insert result = new Insert(content);
      initialize(result);
      return result;
    }

    public class Insert extends TweetApiRequest<itesm.tweet_api.model.MessagesCodeMessage> {

      private static final String REST_PATH = "insert";

      /**
       * Create a request for the method "tweet.insert".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link Insert#execute()} method to invoke the remote operation.
       * <p> {@link
       * Insert#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)} must
       * be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesTweetInput}
       * @since 1.13
       */
      protected Insert(itesm.tweet_api.model.MessagesTweetInput content) {
        super(TweetApi.this, "POST", REST_PATH, content, itesm.tweet_api.model.MessagesCodeMessage.class);
      }

      @Override
      public Insert setAlt(java.lang.String alt) {
        return (Insert) super.setAlt(alt);
      }

      @Override
      public Insert setFields(java.lang.String fields) {
        return (Insert) super.setFields(fields);
      }

      @Override
      public Insert setKey(java.lang.String key) {
        return (Insert) super.setKey(key);
      }

      @Override
      public Insert setOauthToken(java.lang.String oauthToken) {
        return (Insert) super.setOauthToken(oauthToken);
      }

      @Override
      public Insert setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Insert) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Insert setQuotaUser(java.lang.String quotaUser) {
        return (Insert) super.setQuotaUser(quotaUser);
      }

      @Override
      public Insert setUserIp(java.lang.String userIp) {
        return (Insert) super.setUserIp(userIp);
      }

      @Override
      public Insert set(String parameterName, Object value) {
        return (Insert) super.set(parameterName, value);
      }
    }
    /**
     * Create a request for the method "tweet.list".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link List#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesToken}
     * @return the request
     */
    public List list(itesm.tweet_api.model.MessagesToken content) throws java.io.IOException {
      List result = new List(content);
      initialize(result);
      return result;
    }

    public class List extends TweetApiRequest<itesm.tweet_api.model.MessagesTweetList> {

      private static final String REST_PATH = "list";

      /**
       * Create a request for the method "tweet.list".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link List#execute()} method to invoke the remote operation. <p>
       * {@link List#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)}
       * must be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesToken}
       * @since 1.13
       */
      protected List(itesm.tweet_api.model.MessagesToken content) {
        super(TweetApi.this, "POST", REST_PATH, content, itesm.tweet_api.model.MessagesTweetList.class);
      }

      @Override
      public List setAlt(java.lang.String alt) {
        return (List) super.setAlt(alt);
      }

      @Override
      public List setFields(java.lang.String fields) {
        return (List) super.setFields(fields);
      }

      @Override
      public List setKey(java.lang.String key) {
        return (List) super.setKey(key);
      }

      @Override
      public List setOauthToken(java.lang.String oauthToken) {
        return (List) super.setOauthToken(oauthToken);
      }

      @Override
      public List setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (List) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public List setQuotaUser(java.lang.String quotaUser) {
        return (List) super.setQuotaUser(quotaUser);
      }

      @Override
      public List setUserIp(java.lang.String userIp) {
        return (List) super.setUserIp(userIp);
      }

      @Override
      public List set(String parameterName, Object value) {
        return (List) super.set(parameterName, value);
      }
    }
    /**
     * Create a request for the method "tweet.patch".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link Patch#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesTweetUpdate}
     * @return the request
     */
    public Patch patch(itesm.tweet_api.model.MessagesTweetUpdate content) throws java.io.IOException {
      Patch result = new Patch(content);
      initialize(result);
      return result;
    }

    public class Patch extends TweetApiRequest<itesm.tweet_api.model.MessagesCodeMessage> {

      private static final String REST_PATH = "update";

      /**
       * Create a request for the method "tweet.patch".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link Patch#execute()} method to invoke the remote operation.
       * <p> {@link
       * Patch#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)} must
       * be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesTweetUpdate}
       * @since 1.13
       */
      protected Patch(itesm.tweet_api.model.MessagesTweetUpdate content) {
        super(TweetApi.this, "PATCH", REST_PATH, content, itesm.tweet_api.model.MessagesCodeMessage.class);
      }

      @Override
      public Patch setAlt(java.lang.String alt) {
        return (Patch) super.setAlt(alt);
      }

      @Override
      public Patch setFields(java.lang.String fields) {
        return (Patch) super.setFields(fields);
      }

      @Override
      public Patch setKey(java.lang.String key) {
        return (Patch) super.setKey(key);
      }

      @Override
      public Patch setOauthToken(java.lang.String oauthToken) {
        return (Patch) super.setOauthToken(oauthToken);
      }

      @Override
      public Patch setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Patch) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Patch setQuotaUser(java.lang.String quotaUser) {
        return (Patch) super.setQuotaUser(quotaUser);
      }

      @Override
      public Patch setUserIp(java.lang.String userIp) {
        return (Patch) super.setUserIp(userIp);
      }

      @Override
      public Patch set(String parameterName, Object value) {
        return (Patch) super.set(parameterName, value);
      }
    }
    /**
     * Create a request for the method "tweet.update".
     *
     * This request holds the parameters needed by the tweet_api server.  After setting any optional
     * parameters, call the {@link Update#execute()} method to invoke the remote operation.
     *
     * @param content the {@link itesm.tweet_api.model.MessagesTweetUpdate}
     * @return the request
     */
    public Update update(itesm.tweet_api.model.MessagesTweetUpdate content) throws java.io.IOException {
      Update result = new Update(content);
      initialize(result);
      return result;
    }

    public class Update extends TweetApiRequest<itesm.tweet_api.model.MessagesCodeMessage> {

      private static final String REST_PATH = "update";

      /**
       * Create a request for the method "tweet.update".
       *
       * This request holds the parameters needed by the the tweet_api server.  After setting any
       * optional parameters, call the {@link Update#execute()} method to invoke the remote operation.
       * <p> {@link
       * Update#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)} must
       * be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link itesm.tweet_api.model.MessagesTweetUpdate}
       * @since 1.13
       */
      protected Update(itesm.tweet_api.model.MessagesTweetUpdate content) {
        super(TweetApi.this, "POST", REST_PATH, content, itesm.tweet_api.model.MessagesCodeMessage.class);
      }

      @Override
      public Update setAlt(java.lang.String alt) {
        return (Update) super.setAlt(alt);
      }

      @Override
      public Update setFields(java.lang.String fields) {
        return (Update) super.setFields(fields);
      }

      @Override
      public Update setKey(java.lang.String key) {
        return (Update) super.setKey(key);
      }

      @Override
      public Update setOauthToken(java.lang.String oauthToken) {
        return (Update) super.setOauthToken(oauthToken);
      }

      @Override
      public Update setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Update) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Update setQuotaUser(java.lang.String quotaUser) {
        return (Update) super.setQuotaUser(quotaUser);
      }

      @Override
      public Update setUserIp(java.lang.String userIp) {
        return (Update) super.setUserIp(userIp);
      }

      @Override
      public Update set(String parameterName, Object value) {
        return (Update) super.set(parameterName, value);
      }
    }

  }

  /**
   * Builder for {@link TweetApi}.
   *
   * <p>
   * Implementation is not thread-safe.
   * </p>
   *
   * @since 1.3.0
   */
  public static final class Builder extends com.google.api.client.googleapis.services.json.AbstractGoogleJsonClient.Builder {

    /**
     * Returns an instance of a new builder.
     *
     * @param transport HTTP transport, which should normally be:
     *        <ul>
     *        <li>Google App Engine:
     *        {@code com.google.api.client.extensions.appengine.http.UrlFetchTransport}</li>
     *        <li>Android: {@code newCompatibleTransport} from
     *        {@code com.google.api.client.extensions.android.http.AndroidHttp}</li>
     *        <li>Java: {@link com.google.api.client.googleapis.javanet.GoogleNetHttpTransport#newTrustedTransport()}
     *        </li>
     *        </ul>
     * @param jsonFactory JSON factory, which may be:
     *        <ul>
     *        <li>Jackson: {@code com.google.api.client.json.jackson2.JacksonFactory}</li>
     *        <li>Google GSON: {@code com.google.api.client.json.gson.GsonFactory}</li>
     *        <li>Android Honeycomb or higher:
     *        {@code com.google.api.client.extensions.android.json.AndroidJsonFactory}</li>
     *        </ul>
     * @param httpRequestInitializer HTTP request initializer or {@code null} for none
     * @since 1.7
     */
    public Builder(com.google.api.client.http.HttpTransport transport, com.google.api.client.json.JsonFactory jsonFactory,
        com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
      super(
          transport,
          jsonFactory,
          DEFAULT_ROOT_URL,
          DEFAULT_SERVICE_PATH,
          httpRequestInitializer,
          false);
      //setBatchPath(DEFAULT_BATCH_PATH);
    }

    /** Builds a new instance of {@link TweetApi}. */
    @Override
    public TweetApi build() {
      return new TweetApi(this);
    }

    @Override
    public Builder setRootUrl(String rootUrl) {
      return (Builder) super.setRootUrl(rootUrl);
    }

    @Override
    public Builder setServicePath(String servicePath) {
      return (Builder) super.setServicePath(servicePath);
    }
/*
    @Override
    public Builder setBatchPath(String batchPath) {
      return (Builder) super.setBatchPath(batchPath);
    }
*/

    @Override
    public Builder setHttpRequestInitializer(com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
      return (Builder) super.setHttpRequestInitializer(httpRequestInitializer);
    }

    @Override
    public Builder setApplicationName(String applicationName) {
      return (Builder) super.setApplicationName(applicationName);
    }

    @Override
    public Builder setSuppressPatternChecks(boolean suppressPatternChecks) {
      return (Builder) super.setSuppressPatternChecks(suppressPatternChecks);
    }

    @Override
    public Builder setSuppressRequiredParameterChecks(boolean suppressRequiredParameterChecks) {
      return (Builder) super.setSuppressRequiredParameterChecks(suppressRequiredParameterChecks);
    }

    @Override
    public Builder setSuppressAllChecks(boolean suppressAllChecks) {
      return (Builder) super.setSuppressAllChecks(suppressAllChecks);
    }

    /**
     * Set the {@link TweetApiRequestInitializer}.
     *
     * @since 1.12
     */
    public Builder setTweetApiRequestInitializer(
        TweetApiRequestInitializer tweetapiRequestInitializer) {
      return (Builder) super.setGoogleClientRequestInitializer(tweetapiRequestInitializer);
    }

    @Override
    public Builder setGoogleClientRequestInitializer(
        com.google.api.client.googleapis.services.GoogleClientRequestInitializer googleClientRequestInitializer) {
      return (Builder) super.setGoogleClientRequestInitializer(googleClientRequestInitializer);
    }
  }
}
